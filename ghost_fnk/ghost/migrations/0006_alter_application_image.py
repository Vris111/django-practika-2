# Generated by Django 4.2.7 on 2023-11-18 03:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0005_alter_application_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='user/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'], message='Allowed types: bmp, jpeg, jpg. png')]),
        ),
    ]