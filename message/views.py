from django.shortcuts import render
from django.db.models import Q
from .models import *
 

def message(request):
    chats = Chat.objects.filter(
        Q(message__from_user=request.user) |
        Q(message__to_user=request.user) 
    ).distinct()
    return render(request, "message.html", {"chats": chats})


def chat(request, id):
    chat_obj = Chat.objects.get(id=id)
    context = {"chat":chat_obj}
    return render(request, "chat.html", context)