import django_filters
from friendship.models import Friend
from .models import *


class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ["username"]


class FriendFilter(django_filters.FilterSet):
    class Meta:
        model = Friend
        fields = ["to_user"]
