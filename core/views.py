from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from core.forms import *
from .models import *


@login_required(login_url="sign_up")
def news(request):
    return render(request, "base.html", )




@login_required(login_url="sign_up")
def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    return render(request, "core/profile.html", context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect(news)
    context = {} 
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(news)

    context["form"] = AuthenticationForm()
    return render(request, "core/sign_up.html" , context)

def sign_out(request):
    auth.logout(request)
    return redirect(sign_up)



def registration(request):
    context = {}
   
    if request.method == "POST":
       form = RegistrationForm(request.POST)
       password1 = request.POST["password1"]
       password2 = request.POST["password2"]
       if form.is_valid():
          form.save()
          return redirect("sign_up")

    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)




def edit(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("news")

    context = {}
    context["form"] = ProfileEditForm(instance=profile)

    return render(
        request,
        "core/form.html",
        context
    )
        

    