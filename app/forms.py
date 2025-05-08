# app/forms.py

from django import forms

class LocalLoginForm(forms.Form):
    user_id = forms.CharField(label="아이디", max_length=100)
    user_pw = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
