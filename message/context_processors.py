from .models import *
from django.db.models import Q


def chats(request):
    chats = Chat.objects.filter(
        Q(message__from_user=request.user) |
        Q(message__to_user=request.user) 
    ).distinct()
    return {"chats": chats}
