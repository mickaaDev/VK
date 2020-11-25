from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = [
        'text',
        'publication_com',
        'user',
        'likes'
    ]


admin.site.register(Comment)
