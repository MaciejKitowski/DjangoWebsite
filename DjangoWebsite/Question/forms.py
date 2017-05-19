from django.contrib.auth.forms import AuthenticationForm 
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'})
    )
    password = forms.CharField(
        label = "Username",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'})
    )