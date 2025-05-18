# app/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'), 
    
    # 페이지 이동요청
    path('main_page/', views.main_page, name='main_page'),
    path('main/', views.main_page, name='main_page'),
    path("login_page/", views.login_page, name = 'login_page'),
    path("register_page/", views.register_page, name = 'register_page'),
    path("find_id/", views.find_id, name = 'find_id'),
    path("find_pw/", views.find_pw, name = 'find_pw'),
    path("manual/", views.manual, name = 'manual'),

    # 기능 처리요청
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('coin_value/', views.coin_live_value, name='coin_value'),
    path('trade_request/' , views.trade_order_request, name='coin_buy_request'),
]
