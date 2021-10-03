from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'password_short': _('The password is too short.'),
        'password_space': _('No spaces in password.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        if ' ' in password1:
            raise ValidationError(
                self.error_messages['password_space'],
                code='password_space',
            )
        if len(password1) < 8:
            raise ValidationError(
                self.error_messages['password_short'],
                code='password_short'
            )
        return password2


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image', 'bio', 'relationship', 'families', 'city', 'gender', 'bday',]

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     user_count = User.objects.filter(email=email).count()
    #     if user_count > 0:
    #         raise forms.ValidationError("This email has already been registered. Please check and try again or "
    #                                     "reset your password.")
    #     return email
