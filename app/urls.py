# app/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'), 
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login, name='local_login'),  # 로컬 로그인
    path('auth/complete/google-oauth2/', views.complete_google, name='complete_google'),  # 구글 로그인
    
    # 페이지 이동요청
    path('main_page/', views.main_page, name='main_page'),
    path("login_page/", views.login_page, name = 'login_page'),
    path("register_page/", views.register_page, name = 'register_page'),
    path("find_id/", views.find_id, name = 'find_id'),
    path("find_pw/", views.find_pw, name = 'find_pw'),
    path("manual/", views.manual, name = 'manual'),

    # 페이지 처리요청
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]