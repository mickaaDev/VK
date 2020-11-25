from django.conf.urls import include
from django.urls import path
from .views import *
from comments.views import *

urlpatterns = [
    path("", albums, name="albums"),
    path("album_create/",create_album,name="create_album"),
    path("create_item/",create_gallery_item,name="create_gallery_item"),
    path("album/<int:pk>/", album, name="album"),
    path("detail_item/<int:pk>/",detail_gallery,name="detail_gallery"),
    path("item/<int:pk>/delete/", delete_item, name="delete_item"),
]