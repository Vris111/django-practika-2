# Generated by Django 4.2.7 on 2023-11-17 04:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Application name')),
                ('description', models.CharField(max_length=254, verbose_name='Application description')),
                ('status', models.CharField(choices=[('N', 'New'), ('ATJ', 'Accepted the job'), ('D', 'Done')], default='N', max_length=150, verbose_name='Appication status')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='/media/default.jpeg', height_field=50, upload_to='user/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(['bmp', 'jpeg', 'jpg', 'png'], message='Allowed types: bmp, jpeg, jpg. png')], width_field=100)),
                ('category', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='ghost.category', verbose_name='Application category')),
            ],
        ),
    ]