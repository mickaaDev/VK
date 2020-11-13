
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User 
from django.urls import reverse 
from django.views.generic import View 

from .models import *
from .forms import *
 
 
# Create your views here.
def edit_comment(request,pk):
    comment = Comment.objects.get(pk=pk)
    if request.method  == "POST":
        form = CommentForm(request.POST , instance=comment)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    
    form = CommentForm(instance=comment)
    return render(request, "publication/comment_form.html",{'form':form})

def delete_comment(request,pk):
    Comment.objects.get(pk=pk).delete()
    return render(request,"success.html")



