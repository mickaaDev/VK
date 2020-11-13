from django.conf.urls import include
from django.urls import path
from .views import *
from comments.views import *

urlpatterns = [
    path("all/", publications , name="publications"),
    path("<int:pk>/", detail_publication , name="detail_publication"),
    path("create/",publication_create, name="publication-create"),
    path("edit/<int:pk>/", edit_publication, name="edit-publication"),
    path("comment/<int:pk>/edit/",edit_comment , name="edit-comment"),
    path("comment/<int:pk>/delete/",delete_comment , name="delete-comment")
]