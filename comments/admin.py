from django.contrib import admin
from .models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = [
        'text',
        'publication_com',
        'user',
        'likes'
    ]

class CommmentToCommnet(admin.ModelAdmin):
    model = Comment_to_comment
    list_display = [
        'text',
        'comment',
        'user',
        'likes'
    ]

admin.site.register(Comment)
admin.site.register(Comment_to_comment)