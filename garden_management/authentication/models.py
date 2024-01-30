from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


# username認証をemail認証に変更するため、UserManagerをオーバーライドする。
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user


# カスタムユーザモデル
class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True, editable=False)
    nickname = models.CharField(max_length=127, verbose_name="ニックネーム")
    email = models.EmailField(unique=True, verbose_name="メールアドレス")

    # ユーザの利用可否（ログイン可否）を保存するfield。
    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    username_validator = UnicodeUsernameValidator()
    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("nickname",)

    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        try:
            send_mail(
                subject,
                message,
                from_email,
                [self.email],
                **kwargs
            )
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
