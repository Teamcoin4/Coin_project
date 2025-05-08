from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib import messages
from .forms import LocalLoginForm
from .models import LocalUser
from django.contrib.auth.hashers import make_password, check_password


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
    return render(request, 'main_page', {'form': form})

# 로그아웃 기능
def logout(request):
    request.session.flush()  # 모든 세션 데이터를 한 줄로 제거
    return redirect('login_page')

# 회원가입 페이지 호출
def register_page(request):
    return render(request, 'register_page.html')
=======
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from app.models import User
import json

# Create your views here.

# 메인 페이지 호출
def main_page(request):
    return render(request, 'main_page.html')

# 로그인 페이지 호출
def login_page(request):
    return render(request, 'login_page.html')

# 로그인 데이터 처리
def login(request):
    if request.method == 'POST':
        print('login POST 요청처리')
        loginID = request.POST.get('loginID')
        loginPW = request.POST.get('loginPW')
        
        try:
            # 데이터베이스에서 사용자 조회 (Register 모델 사용)
            user = User.objects.get(user_id=loginID)
            
            # 비밀번호 확인
            if user.user_pw == loginPW:  # 실제 환경에서는 암호화된 비밀번호 비교 필요
                # 로그인 성공 - 세션에 사용자 정보 저장
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.user_name
                request.session['is_admin'] = user.is_admin
                request.session['is_logged_in'] = True
                
                print('@@@@@@@@@@@@@@@@@@@@@@로그인 성공@@@@@@@@@@@@@@@@@@@@@@')
                return redirect('main_page')  # 메인 페이지로 리다이렉트
            else:
                # 비밀번호 불일치
                print('@@@@@@@@@@@@@@@@@@@@@@비밀번호 불일치@@@@@@@@@@@@@@@@@@@@@@')
                messages.error(request, '비밀번호가 일치하지 않습니다.')
                return render(request, 'login_page.html')
                
        except User.DoesNotExist:
            # 사용자 ID 없음
            print('@@@@@@@@@@@@@@@@@@@@@@사용자 ID 없음@@@@@@@@@@@@@@@@@@@@@@')
            messages.error(request, '존재하지 않는 사용자 ID입니다.')
            return render(request, 'login_page.html')
    else:
        # GET 요청
        print('@@@@@@@@@@@@@@@@@@@@@@로그인 페이지 로드@@@@@@@@@@@@@@@@@@@@@@')
        return render(request, 'login_page.html')

# 로그아웃 기능
def logout(request):
    # 세션에서 사용자 정보 제거
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    if 'is_admin' in request.session:
        del request.session['is_admin']
    if 'is_logged_in' in request.session:
        del request.session['is_logged_in']
    
    # 로그인 페이지로 리다이렉트
    return redirect('main_page')

# 메인 페이지 함수
def main_page(request):
    # 로그인 상태 확인
    if not request.session.get('is_logged_in', False):
        messages.error(request, '로그인이 필요합니다.')
        return redirect('login')
    
    # 로그인된 사용자 정보 가져오기
    user_id = request.session.get('user_id')
    
    try:
        user = User.objects.get(user_id=user_id)
        context = {
            'user': user
        }
        return render(request, 'main_page.html', context)
    except User.DoesNotExist:
        # 세션에 있는 사용자 정보가 DB에 없는 경우
        messages.error(request, '사용자 정보가 유효하지 않습니다.')
        return redirect('login')


# 회원가입 페이지 호출
def register_page(request):
    context = {}
    return render(request, 'register_page.html', context)
>>>>>>> 15cec77dde070bf51d70866b6249d406a96f8e64

# 회원가입 데이터 처리
def register(request):
    if request.method == 'POST':
<<<<<<< HEAD
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
=======
        print('register POST 요청처리')
        registerID = request.POST.get('registerID')
        registerPW = request.POST.get('registerPW')
        registerNAME = request.POST.get('registerNAME')
        registerAdmin = request.POST.get('is_admin', False)  # 값이 없으면 False로 설정
        
        # 이미 존재하는 ID인지 확인
        if User.objects.filter(user_id=registerID).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')
            return render(request, 'register_page.html')

        register = User()
        register.user_id = registerID
        register.user_pw = registerPW
        register.user_name = registerNAME
        register.is_admin = registerAdmin == 'on'  # 체크박스는 'on'일 때 True

        register.save()  # DB에 저장

        print('@@@@@@@@@@@@@@@@@@@@@@회원가입 성공@@@@@@@@@@@@@@@@@@@@@@')
        
        # 회원가입 후 로그인 페이지로 리다이렉트
        messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요.')
        return redirect('login')
    else:
        print('@@@@@@@@@@@@@@@@@@@@@@회원가입 페이지 로드@@@@@@@@@@@@@@@@@@@@@@')
        return render(request, 'register_page.html')
>>>>>>> 15cec77dde070bf51d70866b6249d406a96f8e64
