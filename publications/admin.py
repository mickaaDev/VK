from django.contrib import admin
from .models import * 


class LikeTabularInline(admin.TabularInline):
    model = Like

class PublicationAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInline]
    class Meta:
        model = Publication

admin.site.register(Publication)
admin.site.register(Like)
