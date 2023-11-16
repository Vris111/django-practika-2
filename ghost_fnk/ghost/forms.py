from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from ghost.models import User


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"^[а-яА-Я\s-]+$"
    message = "Enter a valid Full Name. This value may contain only Cyrillic letters, spaces, and dashes."


@deconstructible
class LoginValidator(validators.RegexValidator):
    regex = r"^[a-zA-Z-]+$"
    message = "Enter a valid login. This value may contain only Latin letters and '-'."


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'})),
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'})),
    password1 = forms.CharField(label='Password'),
    password2 = forms.CharField(label='Password'),
    first_name = forms.CharField(label='Name', max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'})),
    last_name = forms.CharField(label='Surname', max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'})),
    patronymic = forms.CharField(label='Patronymic', max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'})),
    agree_to_processing = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'patronymic', 'password1', 'password2', 'agree_to_processing']

    def clean_username(self):
        username = self.cleaned_data['username']
        validator = LoginValidator()
        try:
            validator(username)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose another one.')

        return username
