from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User 
from django.db.models import Q
from django.views.generic import View 

from django.shortcuts import get_object_or_404

from .models import *
# from .form import *

# def publication(request,id):
#     context = {}
#     context["publication"] = Publication.objects.get(id=id)
#     return render(request , "publications/pub.html" ,context)

def publication(request):
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


