from django.conf.urls import include
from django.urls import path
from .views import *


urlpatterns = [
    path("create/",feedback_create,name="feedback_create"),
] 