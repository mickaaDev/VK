from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Comment)
admin.site.register(Comment_to_comment)