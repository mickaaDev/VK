from django.urls import path
from django.conf.urls.static import static 
from .views import *
from comments.views import *
from core.views import *

urlpatterns = [
    path("all/", publications , name="publications"),
    path("<int:pk>/", detail_publication , name="detail_publication"),
    path("create/",publication_create, name="publication-create"),
    path("edit/<int:pk>/", edit_publication, name="edit-publication"),
    path("comment/<int:pk>/edit/",edit_comment , name="edit-comment"),
    path("comment/<int:pk>/delete/",delete_comment , name="delete-comment"),
    path("like_commnet/<int:pk>/",comment_like, name="comment_like"),
    path("like_publication/<int:pk>/",publication_like,name="publication_like")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
