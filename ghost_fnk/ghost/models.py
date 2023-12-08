from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension, FileExtensionValidator
from django.urls import reverse

class User(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Login', unique=True, blank=False)
    first_name = models.CharField(verbose_name="First name", max_length=150, blank=False)
    last_name = models.CharField(verbose_name="Last name", max_length=150, blank=False)
    email = models.EmailField(verbose_name="Email address", blank=False)
    patronymic = models.CharField(max_length=150, verbose_name='Patronymic', blank=False)
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Category name', blank=False, unique=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=150, verbose_name='Application name', blank=False)
    description = models.CharField(max_length=254, verbose_name='Application description', blank=False)
    category = models.ForeignKey("Category", max_length=150, verbose_name='Application category', blank=False,
                                 on_delete=models.CASCADE)
    NEW = 'N'
    ACCEPTED_THE_JOB = 'ATJ'
    DONE = 'D'

    AppStatus = [
        (NEW, 'New'),
        (ACCEPTED_THE_JOB, 'Accepted the job'),
        (DONE, 'Done')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    status = models.CharField(max_length=150, verbose_name='Appication status', choices=AppStatus,
                              default=NEW)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='user/', default='media/default.jpeg',
    validators =[validate_image_file_extension,
                  FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'],
                                         message='Allowed types: bmp, jpeg, jpg. png')])
    image_status = models.ImageField(upload_to='user/', verbose_name='Image for status',default='media/default.jpeg',
    validators =[validate_image_file_extension,
                  FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'],
                                         message='Allowed types: bmp, jpeg, jpg. png')])
    comm = models.CharField(max_length=150, verbose_name='comment', blank=False)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])
