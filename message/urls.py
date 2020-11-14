from django.urls import path
from .views import *

urlpatterns = [
    path("message/", message, name="message"),
    path("chat/<int:id>/", chat, name="chat"),
]