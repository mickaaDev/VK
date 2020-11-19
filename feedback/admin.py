from django.contrib import admin
from .models import *


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [
        "pk",
        "user",
        'text',
        "created",
    ]
    