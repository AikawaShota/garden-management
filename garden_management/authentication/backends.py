from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

CustomUserModel = get_user_model()


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUserModel.objects.get(email=username)
        except CustomUserModel.DoseNotExist:
            return None
        else:
            if (user.check_password(password)
                    and self.user_can_authenticate(user)):
                return user
