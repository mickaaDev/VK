from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def gallery_items(request):
    context = {}
    context["gallery_items"] =  Gallery_item.objects.filter(avialable=True)
    return render(request, "gallery/gallery_items.html", context)

def detail_galery_item(request):
    gallery_item = Gallery_item.objects.get(pk=pk):
    
    if request.method == "POST":
        if "add_comment_btn" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment()
                comment.user = request.user
                comment.gallery_item_com = gallery_item
                comment.text = form.cleaned_data["text"]
                comment.save()

    context = {}
    context["gallery_item"] = Gallery_item.objects.get(pk=pk)
    context["form"] = CommentForm()
    return render(request , "publication/detail_gallery.html", context)
