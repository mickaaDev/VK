from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class MessageImageInline(admin.TabularInline):
    model = MessageImage
    

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["date", "from_user", "to_user", "chat"]
    list_editable = ["chat"]
    inlines = [MessageImageInline]


admin.site.register(Chat)
