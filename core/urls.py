from django.urls import path 
from django.contrib.auth import views as auth_views
#from friendship.views import *
from .views import *


urlpatterns = [
    path("", sign_up, name="sign_up" ),
    path("text/", text, name="text"),
    path("registration/", registration, name="registration"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("sign-out/", sign_out, name="sign-out"),
    path("edit-profile/<int:pk>/", edit_profile , name="edit-profile"),
    path("info/<int:pk>/", info, name="info"),
    path("settings/<int:pk>/", SettingsView.as_view(), name="settings"),
    path("change-password/", change_password, name='change-password'),
    path("new-password/", new_password, name='new-password'),
    path("view-friends/<username>/", view_friends, name="view-friends"),
    path("friendship-add-friend/<to_username>/", friends_add_friend, name="friends-add-friend"),
    path("view-friends/<username>/", view_friends, name="view_friends"),
    path("friend/cancel/<friendship_request_id>/", view=friends_cancel, name="friends_cancel"),
    path("all-users/", all_users, name="friendship-view-users"),
    path("friend/reject/<friendship_request_id>/", view=friends_reject, name="friends_reject",),
    path("friend/request/", view=friends_request_list, name="friends_request_list"),
    path("friend/request/<friendship_request_id>/", view=friends_requests_detail, name="friends_requests_detail"),
    path("friend/add/<to_username>/", view=friends_add_friend, name="friends_add_friend"),
    path("friend/accept/<friendship_request_id>/", view=friends_accept, name="friends_accept"),
    
    
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