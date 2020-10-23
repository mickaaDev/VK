from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path("all/", publication , name="publications"),
    path("<int:pk>/", detail_publication , name="detail_publication")
]