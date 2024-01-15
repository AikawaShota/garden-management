from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'sample@example.com',
                'class': 'input'
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input'
            }
        )
    )

    user_name = forms.CharField(
        required=True,
        max_length=127,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'input'
            }
        )
    )

    class Meta:
        model = models.User
        fields = ('email', 'password1', 'password2', 'user_name')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'sample@example.com',
                'class': 'input'
            }
        )
    )

    password = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
            }
        )
    )
