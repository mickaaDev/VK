from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [
        "pk",
        "name",
        "user",
        "bday",
        "created",
        "updated",
    ]
    search_fields = ["name", "pk"]

    exlude = [
        "full_name", "deleted", "institution"
    ]
