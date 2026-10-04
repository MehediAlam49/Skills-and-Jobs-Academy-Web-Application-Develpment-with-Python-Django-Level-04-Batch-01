from django import forms
from news_portal_app.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass

class newsForm(forms.ModelForm):
    class Meta:
        model=newsModel
        fields='__all__'