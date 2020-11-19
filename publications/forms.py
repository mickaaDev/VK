from django import forms
from .models import * 
from comments.forms import *

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = [
            "description",
            "image",
        ]


 