from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.urls import reverse 
from django.views.generic import View 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
from django.urls import reverse

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


def comment_to_comment(request,pk):
    comment = Comment_to_comment.objects.get(pk=pk)

    if request.method == "POST":
        if "add_toComment_btn" in request.POST:
            form = CommentToCommentForm(request.POST)
            if form.is_valid():
                comment = Comment_to_comment()
                comment.user = request.user
                comment.comment_com = comment
                comment.txt = form.cleaned_data["text"]
                comment.save()

    context = {}
    context["comment"] = Comment_to_comment.objects.get(pk=pk)
    context["form"] = CommentToCommentForm()
    return render(request , "publication/publication.html", context)   


def comment_like(request,pk):
    comment = Comment.objects.get(id=pk)
    comment.likes.add(request.user)
    return render(request,"success.html")

    # return HttpResponseRedirect(reverse('detail_publication', args=[str(pk)]))

