from django.contrib import admin
from .models import * 

class GalleryItemTabularInline(admin.TabularInline):
    model = Gallery_item

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [GalleryItemTabularInline]
