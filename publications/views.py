from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User 
from django.db.models import Q
from django.views.generic import View 

from .models import *
from .forms import PublicationForm

# from django.shortcuts import get_object_or_404

def publications(request):
    context = {}
    context["publications"] = Publication.objects.filter(avialable=True)
    return render(request, "publications.html", context)

def detail_publication(request,pk):
    publication = Publication.objects.get(pk=pk)
    publication.views +=1
    user = request.user
    publication.save()
    context = {}
    context["publication"] = Publication.objects.get(pk=pk)
    
    return render(request , "publication.html", context)

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

    context["form"] = PublicationForm

    return render(request,"form.html",context)
