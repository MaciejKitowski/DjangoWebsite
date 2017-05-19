from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(
        label = "Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username', 'name': 'username'})
    )
    email = forms.CharField(
        label = "E-mail",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'E-mail', 'name': 'email'})
    )
    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password', 'name': 'password1'})
    )
    password2 = forms.CharField(
        label = "Repeat password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repeat password', 'name': 'password2'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
