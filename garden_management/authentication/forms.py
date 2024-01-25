from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
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


class CustomPasswordChangeForm(PasswordChangeForm):
    # 継承元のPasswordChangeFormのfieldをオーバーライド。
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "input",
            }
        ),
    )

    # 継承元のPasswordChangeFormが継承しているSetPasswordFormのfiledをオーバーライド。
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input",
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input",
            }
        ),
    )
