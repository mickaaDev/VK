from django.conf.urls import include
from django.urls import path
from .views import *
from comments.views import *

urlpatterns = [
    path("gallery/all/", publications , name="publications"),
    path("<int:pk>/", detail_galery_item , name="detail_publication"),
]