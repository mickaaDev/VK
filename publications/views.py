from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404

from core.models import *
from core.views import *
from comments.views import *
from .models import *
from .forms import *



def publications(request):
    context = {}
    context["publications"] = Publication.objects.filter(avialable=True)
    return render(request, "publication/publications.html", context)


def detail_publication(request,pk):
    publication = Publication.objects.get(pk=pk)
    publication.views +=1
    user = request.user
    publication.save()

    if request.method == "POST":
        if "add_comment_btn" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment()
                comment.user = request.user
                comment.publication_com = publication
                comment.text = form.cleaned_data["text"]
                comment.save()

    context = {}
    context["publication"] = Publication.objects.get(pk=pk)
    context["form"] = CommentForm()
    return render(request , "publication/publication.html", context)


def delete_publication(request):
    publication = Publication.objects.get(pk=pk)

    if request.method == "POST":
        if "delete_btn" in request.POST:

            publication.avialable = False
            publication.save()
            return redirect(publications)
    
    context = {}
    context["user"] = User.objects.get(pk=pk)
    context["publication"] = Publication.objects.get(pk=pk)
    return render(request , "publication/publication.html", context)

def publication_create(request):
    context = {} 
    if request.method == "POST":
        form = PublicationForm(request.POST or None ,request.FILES or None)
        if form.is_valid():
            form.instance.publisher = request.user
            form.save()
            context["publications"] = Publication.objects.filter(
                avialable=True
            )
            context["message"] = "Публикация успешно добавлена"
            return redirect(publications)
    else:
        publication = PublicationForm()

    context["form"] = PublicationForm

    return render(request,"publication/add_publication.html",context)


def edit_publication(request,pk):
    publication = Publication.objects.get(pk=pk)

    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES,instance=publication)
        if form.is_valid():
            publication.description = form.cleaned_data["description"]
            publication.image = form.cleaned_data["image"]
            publication.save()

            context = {}
            context["publication"] = publication
            context["form"] = PublicationForm()
            context["message"] = "Публикация была изменена"

            return render(request , "success.html",context)

    form = PublicationForm(instance=publication)
    return render(request , "publication/add_publication.html", {"form":form})

def publication_like(request,pk):
    publication = Publication.objects.get(id=pk)
    publication.likes.add(request.user)
    return render(request,"success.html")
