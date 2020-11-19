from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from .models import *
from .forms import *
 

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

def add_message(request):
    if request.method == "POST":
        chat_id = request.POST.get("chat")
        chat = Chat.objects.get(id=chat_id)
        text = request.POST.get("message")
        message = Message(
            chat=chat,
            text=text,
            from_user=request.user
        )
        message.save()
        return redirect(f'/chat/{ chat_id }#end')

    return redirect(message)

class MessageCreate(CreateView):
    def get(self, *args, **kwargs):
      
        context = {}
        context["form"] = MessageForm()

        return render(
            self.request,
            "new_message.html",
            context
        )
    
    def post(self, *args, **kwargs):
        context = {}

        form = MessageForm(self.request.POST, self.request.FILES, )
   
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.from_user = self.request.user
            new_message.save()
            context["messages"] = Message.objects.filter(
            )
            context["message"] = "Please your message"
        return render(self.request, "message.html", context)

class ChatCreate(CreateView):
    def get(self, *args, **kwargs):
      
        context = {}
        context["form"] = ChatForm()

        return render(
            self.request,
            "new_chat.html",
            context
        )
    
    def post(self, *args, **kwargs):
        context = {}

        form = ChatForm(self.request.POST, self.request.FILES, )
   
        if form.is_valid():
            new_message = form.save()
            new_message.from_user = self.request.user
            new_message.save()
            context["messages"] = Message.objects.filter(
            )
            context["message"] = "Please your message"
        return render(self.request, "message.html", context)