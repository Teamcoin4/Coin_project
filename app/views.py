from django.shortcuts import render, redirect
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
