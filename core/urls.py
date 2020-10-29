from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import *




urlpatterns = [
    path("", sign_up, name="sign_up" ),
    path("registration/", registration, name="registration"),
    path("news/", news, name="news"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("sign-out/", sign_out, name="sign-out"),
    path("edit/<int:pk>/", edit , name="edit"),
    path("info<int:pk>/", info, name="info"),
    path("friends/", friends, name="friends"),

    path("reset_password/", 
        auth_views.PasswordResetView.as_view(template_name="core/password_reset/password_reset.html"), 
        name="reset_password" ),
  
    path("reset_password_sent/", 
        auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset/password_reset_sent.html"), 
        name="password_reset_done" ),
  
    path("reset/<uidb64>/<token>", 
        auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset/password_reset_form.html"), 
        name="password_reset_confirm" ),
  
    path("reset_password_complete/", 
        auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset/password_reset_done.html"), 
        name="password_reset_complete" ),

]