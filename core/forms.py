from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", ]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "photo",
            "user",
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