from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
      'required': 'Sorry, you will need an email'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", 'password1']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('Username already exists')
        return username

    error_messages = {
        'password_mismatch': 'Пароли не совпадают.',
        'password_short': 'Пароль слишком короткий.',
        'space_in_password': 'Пароль не должен содердать пробелы'
    }

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        if ' ' in password1:
            raise ValidationError(
                self.error_messages['space_in_password'],
                code='space_in_password'
            )
        if len(password2) < 7:
            raise ValidationError(
                self.error_messages['password_short'],
                code='password_short'
            )
        return password2


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [

            "photo",
            "name",
            "bday",
            "description",
            "city",
            "gender",
            "institution",
            "relationship",
            "language",
            "families"
        ]


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken'
            )
        return email


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))
    error_messages = {
        'password_missmatch': 'Passwords mismatch.',
        'password_short': 'Password is too short.',
        'space_in_password': 'Password should not contain spaces.'
    }

    def clean_password2(self):
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')
        if pwd2 and pwd1 and pwd1 != pwd2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        if ' ' in pwd1:
            raise ValidationError(
                self.error_messages['space_in_password'],
                code='space_in_password'
            )
        if len(pwd2) < 7:
            raise ValidationError(
                self.error_messages['password_short'],
                code='password_short'
            )
        return pwd2
