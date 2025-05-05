from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserManager(BaseUserManager):
    def create_user(self, user_id, user_pw, user_name, is_admin=False):
        if not user_id:
            raise ValueError('아이디는 필수입니다')
        user = self.model(
            user_id=user_id,
            user_name=user_name,
            is_admin=is_admin
        )
        user.set_password(user_pw)  # 해시된 비밀번호 저장
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_pw, user_name):
        return self.create_user(user_id, user_pw, user_name, is_admin=True)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, primary_key=True)  # 아이디
    user_pw = models.CharField(max_length=128)  # 해시된 비밀번호
    user_name = models.CharField(max_length=100)  # 사용자 이름
    is_admin = models.BooleanField(default=False)  # 관리자 여부

    objects = UserManager()

    USERNAME_FIELD = 'user_id'  # 로그인 시 사용할 필드
    REQUIRED_FIELDS = ['user_name']  # 필수 입력 필드 (비밀번호는 포함되지 않음)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.user_id

    # 실제 DB에 저장되는 password 필드를 user_pw로 매핑
    @property
    def password(self):
        return self.user_pw
    
    @password.setter
    def password(self, raw_password):
        self.user_pw = make_password(raw_password)
        
    def set_password(self, raw_password):
        self.password = raw_password
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.user_pw)



    # Django가 아래 속성들을 요구하므로 가짜로 정의
    # 오류방지용 가짜 속성들
    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return False

    @is_superuser.setter
    def is_superuser(self, value):
        pass

    @property
    def last_login(self):
        return None

    @last_login.setter
    def last_login(self, value):
        pass