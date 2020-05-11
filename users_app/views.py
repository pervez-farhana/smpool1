from django.shortcuts import render , redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomForm
from django.contrib import messages

def register(request):
    
    if request.method=="POST":
       register_form= CustomForm(request.POST)
       if register_form.is_valid():
           register_form.save()
           messages.success(request,("new user account created"))
           return redirect('register') 
    register_form= CustomForm()
    return render(request,'register.html', {'register_form' : register_form})

# Create your views here.
