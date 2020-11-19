from django.contrib import admin
from .models import * 

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery_item
    list_display = [
        'publisher',
        'description',
        'image',
        'likes',
        'created',
        'avialable'
    ]

