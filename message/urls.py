from django.urls import path
from .views import *

urlpatterns = [
    path("message/", message, name="message"),
    path("chat/<int:id>/", chat, name="chat"),
    path("add-message/", add_message, name="add-message"),
    path("create/", MessageCreate.as_view(), name="create-message"),
    #path("create/", create_message, name="create-message"),
]