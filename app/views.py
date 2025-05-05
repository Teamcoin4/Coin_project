from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from app.models import User
from social_django.models import UserSocialAuth
from social_django.utils import psa

# Create your views here.

User = get_user_model()

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
    return render(request, 'login_page.html')

# 로그인 데이터 처리 (로컬 로그인)
def login(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id')
        login_pw = request.POST.get('login_pw')

        try:
            user = User.objects.get(user_id=login_id)
        except User.DoesNotExist:
            messages.error(request, '존재하지 않는 아이디입니다.')
            return render(request, 'login_page.html')

        # 비밀번호 비교
        if user.check_password(login_pw):
            auth_login(request, user)
            messages.success(request, '로그인 성공!')
            return redirect('main_page')
        else:
            messages.error(request, '비밀번호가 올바르지 않습니다.')
            return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')

# 구글 로그인 완료 후 처리 (소셜 로그인)
@psa('social:complete')  # social_django의 'complete' URL을 처리하는 데코레이터
def complete_google(request, backend):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, "구글 로그인에 실패했습니다.")
        return redirect('login_page')

    # 소셜 로그인 정보를 가져옴 (구글 로그인 후 이메일을 가져오기)
    social_user = user.social_auth.get(provider='google')

    # 구글 이메일을 user_id로 사용하기
    email = social_user.extra_data.get('email', None)
    if not email:
        messages.error(request, '구글 계정에 이메일이 없습니다.')
        return redirect('login_page')

    # 이메일을 user_id로 설정하고 로그인 처리
    user.user_id = email
    user.save()
    
    # 로그인 성공 후 메인 페이지로 리다이렉트
    auth_login(request, user)
    messages.success(request, '구글 로그인 성공!')
    return redirect('main_page')

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
        is_admin = request.POST.get('is_admin') == 'True'  # 체크박스를 통해 받은 관리자 권한

        # 필수 항목 확인
        if not register_id or not register_pw or not register_name:
            messages.error(request, '모든 항목을 입력해 주세요.')
            return render(request, 'register_page.html')

        # 아이디 중복 체크
        if User.objects.filter(user_id=register_id).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')
            return render(request, 'register_page.html')

        # 사용자 객체 생성 및 저장
        try:
            user = User.objects.create_user(
                user_id=register_id,
                user_pw=register_pw,
                user_name=register_name,
                is_admin=is_admin
            )
            user.save()
            messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요.')
            return redirect('login_page')
        
        except Exception as e:
            messages.error(request, f'회원가입에 실패했습니다: {e}')
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