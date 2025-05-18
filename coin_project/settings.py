from pathlib import Path
from django.contrib.messages import constants as messages
import os
from dotenv import load_dotenv
import json

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', '.env'))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY is missing! Please set it in the .env file.")
DEBUG = True
ALLOWED_HOSTS = []

# 로그인 관련 설정
LOGIN_URL = '/login_page/'
LOGIN_REDIRECT_URL = '/main_page/'  # 로그인 성공 시 이동
LOGOUT_REDIRECT_URL = '/login_page/'

# 세션 설정
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 3600
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# 메시지 태그 설정
MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'social_django',
]

#pip install django-apscheduler
###scheduler
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

SCHEDULER_DEFAULT = True
###

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.kakao.KakaoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# 프로젝트의 URL 라우팅을 정의하는 파일
ROOT_URLCONF = 'coin_project.urls' 

WSGI_APPLICATION = 'coin_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE"),
        'NAME': os.getenv("NAME"),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT"),
        'OPTIONS': {
            'init_command': os.getenv("init_command")
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 소셜 로그인 관련 키 (실제 값은 개인 키로 설정 필요)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = json.loads(os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE", '["email", "profile"]'))

SOCIAL_AUTH_KAKAO_KEY = os.getenv("SOCIAL_AUTH_KAKAO_KEY")
SOCIAL_AUTH_KAKAO_SECRET = os.getenv("SOCIAL_AUTH_KAKAO_SECRET")

# 소셜 로그인에서 사용할 모델 설정 (카카오, 구글)
SOCIAL_AUTH_USER_MODEL = 'auth.User'  # 소셜 로그인 모델 사용

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
