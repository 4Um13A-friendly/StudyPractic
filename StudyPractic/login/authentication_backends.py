from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Пытаемся найти пользователя по полю 'login'
            user_model = get_user_model()
            user = user_model.objects.get(login=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None