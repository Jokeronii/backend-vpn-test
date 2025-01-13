from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.conf import settings

class CustomPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def encode(self, password, salt, iterations=None):
        secret_key = settings.SECRET_KEY
        return super().encode(password + secret_key, salt, iterations)

    def verify(self, password, encoded):
        secret_key = settings.SECRET_KEY
        return super().verify(password + secret_key, encoded)