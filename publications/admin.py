from django.contrib import admin
from .models import * 


class LikeTabularInline(admin.TabularInline):
    model = Like

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInline]


# admin.site.register(Publication, PublicationAdmin)
