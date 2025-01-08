from django import forms
from django.forms import ModelForm
from  django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)