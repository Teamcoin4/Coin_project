# coin_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),  # 기본 앱
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
]