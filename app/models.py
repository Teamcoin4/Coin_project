from django.db import models

# 유저 회원가입 데이터
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'     # 테이블 이름 수동 지정
        managed = False       # Django가 이 테이블을 관리하지 않음
        app_label = 'app'     # 앱 레이블 명시

    def __str__(self):
        return 'id : {}, pw : {}, name : {}, admin : {}'.format(
            self.user_id, self.user_pw, self.user_name, self.is_admin
        )