# from django.contrib.auth import password_validation
# from django.core.exceptions import ValidationError
# from django.forms import forms
# from .models import user_registrated, User
# from django.db import models
#
#
# class RegisterUserForm(forms.Form):
#     email = models.CharField(max_length=254, verbose_name='E-mail', unique=True, blank=False),
#     password1 = models.CharField(label='Password', blank=False, help_text=password_validation.password_validators_help_text_html())
#     password2 = models.CharField(label='Password (repeat)', blank=False, help_text='Pleas repeat your password')
#
#     def clean_password1(self):
#         password1 = self.cleaned_data['password1']
#         if password1:
#             password_validation.validate_password(password1)
#         return password1
#
#     def clean(self):
#         super().clean()
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
#         if password1 and password2 and password1 != password2:
#             errors = {'password2': ValidationError(
#                 'The entered passwords do not match', code='password_mismatch'
#             )}
#             raise ValidationError(errors)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         user.is_active = False
#         user.is_activated = False
#         if commit:
#             user.save()
#         user_registrated.send(RegisterUserForm, instance=user)
#         return user
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_messages')
