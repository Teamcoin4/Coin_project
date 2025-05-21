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
    
    class Meta:
        db_table = "user"
        indexes = [
            models.Index(fields=["user_id"]),
        ]

class coin_recent(models.Model):
    coin_name = models.CharField(max_length=10, primary_key=True)
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    time_stamp = models.DateTimeField()
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    candle_time_kst = models.DateTimeField(auto_now_add=True)
    interval = models.CharField(max_length=10)


    class Meta:
        db_table = "coin_recent"
        indexes = [
            models.Index(fields=["coin_name", "time_stamp"]),
        ]


class coin_archive(models.Model):
    coin_name = models.CharField(max_length=10)
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    time_stamp = models.DateTimeField()
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    candle_time_kst = models.DateTimeField(auto_now_add=True)
    interval = models.CharField(max_length=10)

    class Meta:
        db_table = "coin_archive"
        indexes = [
            models.Index(fields=["coin_name", "time_stamp"]),
        ]

class trade_order_request(models.Model):
    user_id = models.ForeignKey(LocalUser, on_delete=models.CASCADE, db_column='user_id')
    coin_name = models.CharField(max_length=10)
    coin_price = models.FloatField()
    coin_amount = models.FloatField()
    order_time = models.DateTimeField(auto_now_add=True)
    trade_type = models.CharField(max_length=10)  # 'buy' or 'sell'
    order_id = models.FloatField(unique=True)

    class Meta:
        db_table = "trade_request"
        indexes = [
            models.Index(fields=["user_id"])
        ]

class Asset(models.Model):
    user_id = models.ForeignKey(LocalUser, on_delete=models.CASCADE,db_column='user_id')
    coin_name = models.CharField(max_length=10)
    coin_amount = models.FloatField()
    coin_price = models.FloatField()
    total_value = models.FloatField()
    trade_time = models.DateTimeField(auto_now_add=True)
    money = models.FloatField()

    class Meta:
        db_table = "asset"
        indexes = [
            models.Index(fields=["user_id"]),
        ]
    

class trade_history(models.Model):
    user_id = models.ForeignKey(LocalUser, on_delete=models.CASCADE,db_column='user_id')
    coin_name = models.CharField(max_length=10)
    coin_price = models.FloatField()
    coin_amount = models.FloatField()
    order_time = models.DateTimeField()
    trade_time  = models.DateTimeField(auto_now_add=True)
    is_deal = models.BooleanField(default=False)
    trade_fee = models.FloatField(default=0.0)

    class Meta:
        db_table = "trade_history"
        indexes = [
            models.Index(fields=["user_id"])
        ]
