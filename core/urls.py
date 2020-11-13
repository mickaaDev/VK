from django.urls import path 
from django.contrib.auth import views as auth_views
from friendship.views import *
from .views import *


urlpatterns = [
    path("", sign_up, name="sign_up" ),
    path("registration/", registration, name="registration"),
    path("news/", news, name="news"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("sign-out/", sign_out, name="sign-out"),
    path("edit/<int:pk>/", edit , name="edit"),
    path("info/<int:pk>/", info, name="info"),
    path("settings/<int:pk>/", SettingsView.as_view(), name="settings"),
    path("change-password/", change_password, name='change-password'),
    path("view-friends/<username>/", view_friends, name="view-friends"),
    path("friendship-add-friend/<to_username>/", friendship_add_friend, name="friendship-add-friend"),
    path("all-users/", all_users, name="friendship-view-users"),
    path("friend/reject/<friendship_request_id>/", view=friendship_reject, name="friendship_reject",),
    path("friend/requests/", view=friendship_request_list, name="friendship_request_list"),
    
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