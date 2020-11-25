from django import forms
from .models import * 

class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = Gallery_item
        fields = [
            'description',
            'image',
            'album'
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
         model = Album
         fields = ['name']