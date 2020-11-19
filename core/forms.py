from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *




class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email" ]



    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        print (user_count)
        if user_count > 0:
            raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
        return email


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
            email = self.cleaned_data.get("email")
            user_count = User.objects.filter(email=email).count()
            print (user_count)
            if user_count > 0:
                raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
            return email
        
        