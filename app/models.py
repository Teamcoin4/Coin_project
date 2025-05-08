# models.py

from django.db import models
from django.contrib.auth.models import BaseUserManager

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
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
