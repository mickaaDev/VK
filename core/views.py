from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView, UpdateView
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
            print("edited2!")
            form.save()
            return redirect("news")
            print("edited!")

    context = {}
    context["form"] = ProfileEditForm(instance=profile)

    return render(
        request,
        "core/form.html",
        context
    )




@login_required(login_url="sign_up")      
def info(request, pk):
    return render(request, "core/full_profile.html")

    
class FollowersList(ListView):
    model = Profile
    template_name = "core/full_profile.html"
    queryset = Profile.objects.filter(
        subscription=True,
    )


def friends(request):
    friends = Profile.objects.exclude(subscription=True)
    context = {"friends":friends}
    return render(request, "core/friends.html", context)



class SettingsView(UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'core/settings.html'
    form = EmailForm
    queryset = User.objects.all()
    success_url = "/"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(User, pk=pk_)

    def form_valid(self, form):

        return super().form_valid(form)

   
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()

            return redirect("sign_up")

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, "core/password_settings.html", args)
   

   