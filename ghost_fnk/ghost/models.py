from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Login', unique=True, blank=False)
    first_name = models.CharField(verbose_name="First name", max_length=150, blank=False)
    last_name = models.CharField(verbose_name="Last name", max_length=150, blank=False)
    email = models.EmailField(verbose_name="Email address", blank=False)
    patronymic = models.CharField(max_length=150, verbose_name='Patronymic', blank=False)

    def str(self):
        return self.user.username

