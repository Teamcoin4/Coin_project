from django.shortcuts import render, redirect
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

# 회원가입 데이터 처리
def register(request):
    if request.method == 'POST':
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