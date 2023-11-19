from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from ghost.models import User


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"^[а-яА-Я\s-]+$"
    message = "Please enter valid details. This value may contain only Cyrillic letters, spaces, and dashes."


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

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        validator = FIOValidator()
        try:
            validator(first_name)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        validator = FIOValidator()
        try:
            validator(last_name)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return last_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data['patronymic']
        validator = FIOValidator()
        try:
            validator(patronymic)
        except ValidationError:
            raise forms.ValidationError(validator.message)

        return patronymic

class ApplicationChekerForAdmin(forms.ModelForm):
    def clean(self):
        status = self.cleaned_data.get('status')
        if self.instance.status != 'N':
            raise forms.ValidationError({'status': "The status can only be changed for new applications"})
        elif self.instance.status == 'D' and self.instance.image.count() < 1:
            raise forms.ValidationError({'status': "The status - Done need had min 1 image"})


