from django.shortcuts import render ,redirect
from django.contrib.auth.models import User 

from .models import *
from .forms import *

# Create your views here.
# def feedback(request):
#     context = {}
#     context["message"] = "thanks"
#     return request(request,"feedback/feedback_succsess.html", context )
    
    

def feedback_create(request):
    if request.method == 'POST':
       form = FeedbackForm(request.POST,request.FILES)

       if form.is_valid():
           form.instance.user = request.user
           form.save()
           return render(request , 'feedback/feedback_succsess.html')
 
    else:
        form = FeedbackForm()

    return render(request,'feedback/feedback.html',{'form':form})