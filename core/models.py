from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50, verbose_name='El.paštas')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']










