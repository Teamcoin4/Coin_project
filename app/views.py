from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
from .forms import LocalLoginForm
from .models import LocalUser, coin_recent, coin_archive, trade_order_request, trade_history, Asset
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from decimal import Decimal

#pip install requests
import requests
import schedule
import time
import threading
import json

# 메인 페이지 호출
# @login_required(login_url='login_page')  # 로그인 안 했으면 이 URL로 리다이렉트
def main_page(request):
    user = request.user  # 인증된 사용자 객체 가져오기

    # 메시지를 띄우거나 다른 로직 필요하면 추가 가능
    context = {
        'user': user
    }
    return render(request, 'main_page.html', context)

# 로그인 페이지 호출
def login_page(request):
    form = LocalLoginForm()
    return render(request, 'login_page.html', {'form': form})

# 로그인 데이터 처리 (로컬 로그인)
def login(request):
    if request.method == 'POST':
        form = LocalLoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            user_pw = form.cleaned_data['user_pw']
            try:
                user = LocalUser.objects.get(user_id=user_id)
                if check_password(user_pw, user.user_pw):  # 비밀번호 비교
                    request.session['local_user_id'] = user.user_id
                    request.session['money'] = 1000000 # 임시 money값
                    print("로그인에 성공하였습니다.")
                    return redirect('main_page')
                else:
                    form.add_error(None, "아이디 또는 비밀번호가 잘못되었습니다.")
                    print("아이디 또는 비밀번호가 잘못되었습니다.")
            except LocalUser.DoesNotExist:
                form.add_error(None, "아이디 또는 비밀번호가 잘못되었습니다.")
                print("아이디 또는 비밀번호가 잘못되었습니다.")
    else:
        form = LocalLoginForm()
    return render(request, 'login_page.html', {'form': form})

# 로그아웃 기능
def logout(request):
    request.session.flush()  # 모든 세션 데이터를 한 줄로 제거
    return redirect('login_page')

# 회원가입 페이지 호출
def register_page(request):
    return render(request, 'register_page.html')

# 회원가입 데이터 처리
def register(request):
    if request.method == 'POST':
        register_id = request.POST.get('register_id')
        register_pw = request.POST.get('register_pw')
        register_name = request.POST.get('register_name')
        is_admin = request.POST.get('is_admin') == 'True'

        if not register_id or not register_pw or not register_name:
            messages.error(request, '모든 항목을 입력해 주세요.')
            print("모든 항목을 입력해 주세요.")
            return render(request, 'register_page.html')

        if LocalUser.objects.filter(user_id=register_id).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')
            print("이미 사용 중인 아이디입니다.")
            return render(request, 'register_page.html')

        try:
            user = LocalUser.objects.create(
                user_id=register_id,
                user_pw=make_password(register_pw),  # 비밀번호 해싱
                user_name=register_name,
                is_admin=is_admin
            )
            messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요.')
            return redirect('login_page')

        except Exception as e:
            messages.error(request, f'회원가입에 실패했습니다: {e}')
            print("회원가입에 실패했습니다.")
            return render(request, 'register_page.html')
        

# ID찾기 페이지 호출
def find_id(request):
    return render(request, 'find_id.html')

# PW찾기 페이지 호출
def find_pw(request):
    return render(request, 'find_pw.html')

# 사용설명서 페이지 호출
def manual(request):
    return render(request, 'manual.html')


live_coin_data_scheduler_running = False
user_trade_request = list()
coin_data_history = list()

BTC, ETH, XRP, DOGE = None, None, None, None
# 코인 데이터 저장

def main(request):
    global live_coin_data_scheduler_running

    # 스케줄러가 실행 중인지 확인
    if not live_coin_data_scheduler_running:
        # 스케줄러를 별도의 스레드에서 실행
        thread = threading.Thread(target=coin_store_scheduler)
        thread.daemon = True
        thread.start()
        live_coin_data_scheduler_running = True
    return render(request, 'index.html')

def load_coin_data(request):
    coin_data = coin_recent.objects.all()
    coin_data_history = []

    if coin_data.exists():
        for coin in coin_data:
            coin_data_history.append({
                'coin_name': coin.coin_name,
                'opening_price': float(coin.opening_price),
                'high_price': float(coin.high_price),
                'low_price': float(coin.low_price),
                'trade_price': float(coin.trade_price),
                'time_stamp': coin.time_stamp.isoformat(),  # ISO 형식으로 문자열 변환
                'candle_acc_trade_price': float(coin.candle_acc_trade_price),
                'candle_acc_trade_volume': float(coin.candle_acc_trade_volume),
                'candle_date_time_kst': coin.candle_date_time_kst.isoformat() if coin.candle_date_time_kst else None,
            })
        return JsonResponse({'coin_data': coin_data_history})
    else:
        return JsonResponse({'error': 'No data found'}, status=404)

def remove_order(request):
    # 주문을 삭제하는 함수
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        for order in user_trade_request:
            if order['order_id'] == order_id:
                user_trade_request.remove(order)
                break
        return JsonResponse({'status': 'success'})
    else:
        print("Error: Invalid request method")
        return None

def compare_order_and_coin_value_scheduler():
    for order in user_trade_request[:]:  # 리스트 순회 중 제거 방지를 위해 슬라이싱 사용
        # 현재 코인 가격 결정
        if order['coin_name'] == "KRW-BTC":
            coin_value = BTC
        elif order['coin_name'] == "KRW-ETH":
            coin_value = ETH
        elif order['coin_name'] == "KRW-XRP":
            coin_value = XRP
        elif order['coin_name'] == "KRW-DOGE":
            coin_value = DOGE
        else:
            continue  # 해당하는 코인이 없으면 무시

        # 구매 조건 만족
        if order['trade_type'] == 'buy' and order['coin_price'] >= coin_value:
            trade_history.objects.create(
                user_id=order['user_id'],
                coin_name=order['coin_name'],
                coin_price=order['coin_price'],
                coin_amount=order['coin_amount'],
                order_time=order['order_time']
            )
            user_trade_request.remove(order)

        # 판매 조건 만족
        elif order['trade_type'] == 'sell' and order['coin_price'] <= coin_value:
            # 자산 증가 처리
            try:
                asset = Asset.objects.get(user=order['user_id'])
                total_gain = Decimal(order['coin_price']) * Decimal(order['coin_amount'])
                asset.money += total_gain
                asset.save()
            except Asset.DoesNotExist:
                print("?")
                pass

            # 거래 기록 저장
            trade_history.objects.create(
                user_id=order['user_id'],
                coin_name=order['coin_name'],
                coin_price=order['coin_price'],
                coin_amount=order['coin_amount'],
                order_time=order['order_time']
            )
            user_trade_request.remove(order)

    return None


def coin_store_scheduler():
    # 스케줄러를 실행하는 함수 코인저장장
    store_value = schedule.every(1).seconds.do(coin_value_store)
    # schedule.every(1).seconds.do(coin_live_value)
    while True:
        schedule.run_pending()
        
        # time.sleep(1)
        
        if store_value is True: #DB 저장 실패시
            time.sleep(60)  # 1초 대기
        else:
            break
        

def coin_value_store():
    result_arr = fetch_coin_prices()
    if result_arr is not False:

        # API 호출 실패 처리
        if not result_arr:
            print("Warning: fetch_coin_prices() returned None. Skipping this cycle.")
            return False    # 저장 실패 처리
    
        for coin in result_arr:
            # naive datetime → aware datetime으로 변환
            naive_time = datetime.fromtimestamp(coin["timestamp"] / 1000)
            time_aware = timezone.make_aware(naive_time)

            coin_recent.objects.update_or_create(
                coin_name=coin["market"],
                defaults={
                    'opening_price': coin["opening_price"],
                    'high_price': coin["high_price"],
                    'low_price': coin["low_price"],
                    'trade_price': coin["trade_price"],
                    'time_stamp': time_aware,
                    'candle_acc_trade_price': coin["acc_trade_price_24h"],
                    'candle_acc_trade_volume': coin["acc_trade_volume_24h"],
                    'interval': '1s',
                }
            )

            coin_archive.objects.create(
                coin_name=coin["market"],
                opening_price=coin["opening_price"],
                high_price=coin["high_price"],
                low_price=coin["low_price"],
                trade_price=coin["trade_price"],
                time_stamp=time_aware,  # ✅ timezone-aware datetime 사용
                candle_acc_trade_price=coin["acc_trade_price_24h"],
                candle_acc_trade_volume=coin["acc_trade_volume_24h"],
                interval='1s',
            )
        return True
    else:
        return False

def fetch_coin_prices():
    """
    request 없이 호출 가능한 백그라운드용 함수
    """
    url = "https://api.upbit.com"
    param = {  
        'markets': 'KRW-BTC,KRW-ETH,KRW-XRP,KRW-DOGE'
    }
    response = requests.get(url + '/v1/ticker', params=param)
    result_arr = []

    if response.status_code == 200:
        data = response.json()
        global BTC, ETH, XRP, DOGE
        for coin in data:
            result_arr.append({
                "market": coin.get("market"),
                "trade_price": coin.get("trade_price"),
                "opening_price": coin.get("opening_price"),
                "high_price": coin.get("high_price"),
                "low_price": coin.get("low_price"),
                "acc_trade_price_24h": coin.get("acc_trade_price_24h"),
                "acc_trade_volume_24h": coin.get("acc_trade_volume_24h"),
                "timestamp": coin.get("timestamp"),
                "trade_date_kst": coin.get("trade_date_kst"),
            })

            if coin.get("market") == "KRW-BTC":
                BTC = coin.get("trade_price")
            elif coin.get("market") == "KRW-ETH":
                ETH = coin.get("trade_price")
            elif coin.get("market") == "KRW-XRP":
                XRP = coin.get("trade_price")
            elif coin.get("market") == "KRW-DOGE":
                DOGE = coin.get("trade_price")

        return result_arr
    else:
        print("Error:", response.status_code)
        return None

def coin_live_value(request):
    """
    Django view 함수: HTTP 요청에 응답
    """
    result_arr = fetch_coin_prices()
    if result_arr is not None:
        return JsonResponse({'value': result_arr})
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)


def trade_order_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        coin_name = data.POST.get('coin_name')
        coin_price = data.POST.get('coin_price')
        coin_amount = data.POST.get('coin_amount')
        trade_type_buy_sell = data.POST.get('trade_type')
        user = LocalUser.objects.get(user_id=request.session['user_id'])

        try:
            user = LocalUser.objects.get(user_id=request.session['user_id'])
            total_cost = coin_price * coin_amount

            # 구매일 경우 asset에서 돈 차감
            if trade_type_buy_sell == 'buy':
                asset = Asset.objects.get(user=user)

                if asset.money >= total_cost:
                    asset.money -= total_cost
                    asset.save()
                else:
                    return JsonResponse({'error': '보유 자금이 부족합니다.'}, status=400)
            #메모리에 저장
            user_trade_request.append({
                'user_id': user,
                'coin_name': coin_name,
                'coin_price': coin_price,
                'coin_amount': coin_amount,
                'trade_type': trade_type_buy_sell,
                'order_time': datetime.now()
            })
        except LocalUser.DoesNotExist:
            print("??")
            pass

        
        #DB저장 요청
        trade_order_request.objects.create(
            user_id=user,
            coin_name=coin_name,
            coin_price=coin_price,
            coin_amount=coin_amount,
            trade_type = trade_type_buy_sell,
            order_time=datetime.now()
        )
    else:
        print("거래요청 오류")
        return None
