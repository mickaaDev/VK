from django.urls import path 
from .views import *




urlpatterns = [
    path("", sign_up, name="sign_up" ),
    path("registration/", registration, name="registration"),
    path("news/", news, name="news"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("sign-out/", sign_out, name="sign-out"),
    path("edit/<int:id>", edit, name="edit")
]