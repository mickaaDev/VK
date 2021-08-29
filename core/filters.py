import django_filters
from friendship.models import Friend
from django.contrib.auth.models import User


class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = [ "username"]


class FreidFilter(django_filters.FilterSet):
    class Meta:
        model = Friend
        fields = [ "to_user" ]
