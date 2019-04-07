from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from .validators import ASCIIUsernameValidator


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()
