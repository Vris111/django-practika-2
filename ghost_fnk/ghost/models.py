from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.dispatch import Signal
# from .utilities import send_activation_notification


class User(AbstractUser):
   username = models.CharField(max_length=150, verbose_name='Login', unique=True, blank=False)
   first_name = models.CharField(verbose_name="First name", max_length=150, blank=False)
   last_name = models.CharField(verbose_name="Last name", max_length=150, blank=False)
   email = models.EmailField(verbose_name="Email address", blank=False)
   patronymic = models.CharField(max_length=150, verbose_name='Patronymic', blank=False)



# user_registrated = Signal('instance')
#
# def user_registrated_dispatcher(sender, **kwargs):
#    send_activation_notification(kwargs['instance'])
#
# user_registrated.connect(user_registrated_dispatcher)



