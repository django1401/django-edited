from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser, Profile

from captcha.fields import CaptchaField


class CustomUserCreation(UserCreationForm):



    class Meta:
        model = CustomeUser
        fields = ['username','email', 'password1', 'password2']


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(
        label=("Username"),
        strip=False,
    )
    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class CustomUserProfile(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['user', 'id_code', 'first_name', 'last_name','mobile', 'address', 'image']