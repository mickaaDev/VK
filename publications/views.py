from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User 
from django.db.models import Q

from comments.views import *
from .models import *
from .forms import *

# from django.shortcuts import get_object_or_404 

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
        if "delete_btn" in request.POST:
            publication.avialable = False
            publication.save()
            return redirect(publications)
        elif "add_comment_btn" in request.POST:
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

def publication_create(request):
    context = {}
    if request.method == "POST":
        form = PublicationForm(request.POST,request.FILES)
        if form.is_valid():
            new_publication = form.save()
            new_publication.user = request.user
            new_publication.save()
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


