from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import  UpdateView
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from friendship.models import Friend, Follow, Block, FriendshipRequest
from friendship.exceptions import AlreadyExistsError
from django.contrib.auth.models import User
from publications.urls import *
from .filters import SearchFilter , FreidFilter
from django.http import Http404
from publications.views import *
from core.forms import *
from .models import *


try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User


@login_required(login_url="sign_up")
def profile(request,pk):
    context = {}
    user = User.objects.get(id=pk)
    context["user"] = user
    try:
        context["friendship_request"] = FriendshipRequest.objects.get(
            Q(from_user=user, to_user=request.user) |
            Q(from_user=request.user, to_user=user)    
        )
    except:
        pass
    return render(request, "core/profile.html", context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect(publications)
    context = {} 
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(publications)

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
          return redirect("text")

    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)


@login_required(login_url="profile")
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print("edited2!")
            form.save()
            return redirect("publications")
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

@login_required(login_url="sign_up")      
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("sign_up")

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, "core/password_settings.html", context)






@login_required(login_url="sign_up")      
def new_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("sign_up")

    else:
        form = SetPasswordForm(user=request.user)
    context = {'form': form}
    return render(request, "core/new_password.html", context)
   

def get_friendship_context_object_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_NAME", "user")

def get_friendship_context_object_list_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME", "users" )

def view_friends(request, username, template_name="core/my_friends/friends.html"):
    user = get_object_or_404(user_model, username=username)
    friends = Friend.objects.friends(user)
    
    return render(
        request,
        template_name,{
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
            "friends": friends,},)


def all_users(request, template_name="core/my_friends/list.html"):
    users = user_model.objects.all()
    myFilter = SearchFilter(request.GET, queryset=users)
    users = myFilter.qs
    context = {get_friendship_context_object_list_name(): users, 'myFilter':myFilter}
    return render(request,  template_name,  context)

@login_required
def friends_request_list(request, template_name="core/my_friends/requests_list.html"):
    friendship_requests = Friend.objects.requests(request.user)
    return render(request, template_name, {"requests": friendship_requests})


@login_required
def friends_requests_detail(
    request, friendship_request_id, template_name="core/my_friends/request.html"):
    f_request = get_object_or_404(FriendshipRequest, id=friendship_request_id)
    return render(request, template_name, {"friends_request": f_request})
    

@login_required
def friends_cancel(request, friendship_request_id):
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_sent, id=friendship_request_id)
        f_request.cancel()
        return redirect("all_users")
    return redirect(
        "friends_requests_detail", friendship_request_id=friendship_request_id)

@login_required
def friends_reject(request, friendship_request_id):
    """ Reject a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id)
        f_request.reject()
        return redirect("")
    return redirect(
        "friends_requests_detail", friendship_request_id=friendship_request_id
    )


@login_required
def friends_add_friend(
    request, to_username, template_name="core/my_friends/adds.html"):
    """ Create a FriendshipRequest """
    ctx = {"to_username": to_username}

    if request.method == "POST":
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect("publications")

    return render(request, template_name, ctx)

@login_required
def friends_accept(request, friendship_request_id):
    """ Accept a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id)
        f_request.accept()
        return redirect("view_friends", username=request.user.username)

    return redirect(
        "friends_requests_detail", friendship_request_id=friendship_request_id)