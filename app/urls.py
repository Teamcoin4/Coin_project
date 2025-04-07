from django.urls import path
from . import views
from . import views as auth_views

urlpatterns = [
    path('', views.main_page, name='main_page'),

    # 페이지 이동요청
    path("login_page/", views.login_page, name = 'login_page'),
    path("register_page/", views.register_page, name = 'register_page'),

    # 페이지 처리요청
    path('login/', views.login, name='login'),  # 이 줄 추가: login 함수를 'login' 이름으로 등록
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]