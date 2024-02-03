from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation, get_user_model
from django import forms

CustomUserModel = get_user_model()


# ユーザ登録フォーム
class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ("email", "password1", "password2", "nickname")

    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "placeholder": "sample@example.com",
                "class": "input"
            }
        )
    )

    password1 = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input"
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input"
            }
        )
    )

    nickname = forms.CharField(
        required=True,
        max_length=127,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "nickname",
                "placeholder": "nickname",
                "class": "input"
            }
        )
    )


# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "placeholder": "sample@example.com",
                "class": "input"
            }
        )
    )

    password = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "input"
            }
        )
    )


# パスワード変更フォーム
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


# パスワードリセット用メール送信用メールアドレス入力フォーム
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "placeholder": "sample@example.com",
                "class": "input"
            }
        )
    )


# パスワードリセット用パスワード入力フォーム
class CustomPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=255,
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input"
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        max_length=255,
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "input"
            }
        ),
    )


# ユーザ情報編集フォーム
class UserInformationEditForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = (
            "nickname",
            "email"
        )

    nickname = forms.CharField(
        max_length=127,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "nickname",
                "autocomplete": "nickname"
            }
        )
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "input",
                "placeholder": "sample@example.com",
                "autocomplete": "email"
            }
        )
    )
