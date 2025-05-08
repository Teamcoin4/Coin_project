<<<<<<< HEAD
# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class LocalUserManager(BaseUserManager):
    def create_user(self, user_id, user_pw, user_name, is_admin=False):
        user = self.model(
            user_id=user_id,
            user_name=user_name,
            is_admin=is_admin
        )
        user.set_password(user_pw)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_pw, user_name):
        user = self.create_user(
            user_id=user_id,
            user_pw=user_pw,
            user_name=user_name,
            is_admin=True
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class LocalUser(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
=======
from django.db import models

# 유저 회원가입 데이터
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
>>>>>>> 15cec77dde070bf51d70866b6249d406a96f8e64
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

<<<<<<< HEAD
    def __str__(self):
        return self.user_name
=======
    class Meta:
        db_table = 'user'     # 테이블 이름 수동 지정
        managed = False       # Django가 이 테이블을 관리하지 않음
        app_label = 'app'     # 앱 레이블 명시

    def __str__(self):
        return 'id : {}, pw : {}, name : {}, admin : {}'.format(
            self.user_id, self.user_pw, self.user_name, self.is_admin
        )
>>>>>>> 15cec77dde070bf51d70866b6249d406a96f8e64
