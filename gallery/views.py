from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.contrib.auth.models import User 
from django.db.models import Q 

from comments.views import *
from .models import Album, Gallery_item
from .forms import AlbumForm, GalleryItemForm
# Create your views here.

def albums(request):
    context = {}
    context["album"] = Album.objects.all()
    return render(request,"gallery/albums.html",context)

def create_gallery_item(request):
    context = {}
    if request.method == "POST":
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.publisher = request.user
            form.save()
            return redirect(albums)
    else:
        gallery_item = GalleryItemForm() 
    
    context["form"] = GalleryItemForm
    return render(request,"gallery/gallery_item_create.html",context)


def album(request,pk):
    context = {}
    album = Album.objects.get(id=pk)
    context["object_list"] = Gallery_item.objects.filter(
        album=album,
        avialable=True
    )
    context["album_pk"] = pk
    return render(request,"gallery/albums_info.html",context)

def create_album(request):
    form_class = AlbumForm
    form = form_class(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            name = request.POST.get('name')
            form.save()
            return redirect(albums)
    
    return render(request,"gallery/album_create.html",{'form':form})

def detail_gallery(request,pk):
    context = {}
    context["item"] = Gallery_item.objects.get(pk=pk)
    return render(request , "gallery/detail_item.html", context)


def delete_item(request,pk):
    Gallery_item.objects.get(pk=pk).delete()
    return redirect(albums)
        