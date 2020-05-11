from django.shortcuts import render, redirect
from django.http import HttpResponse
from smpool_app.models import smservices
from smpool_app.forms import serviceform
from django.contrib import messages
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def sservices(request):
   
    if request.method == "POST":
       
        form = serviceform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage=request.user
            instance.save()
            messages.success(request,("entry save"))
        else:
            messages.error(request,("entry error"))
           
        return redirect('services')
    
    
    else:
    
        all_services = smservices.objects.filter(manage=request.user)
        paginator = Paginator(all_services,5)
        page=request.GET.get('pg')
        all_services= paginator.get_page(page)
        return render(request,'services.html',{'all_services': all_services})



def edit_services(request,service_id):
   
    if request.method == "POST":

        sid = smservices.objects.get(pk=service_id)
        form = serviceform(request.POST or None, instance = sid)
        if form.is_valid():
            form.save()
            messages.success(request,("entry Edited!"))
        else:
            messages.error(request,("error in Entry"))
           
        return redirect('services')
    
    
    else:
    
        service_obj = smservices.objects.get(pk=service_id)
        return render(request,'edit.html',{'service_obj': service_obj})


def delete_service(request, service_id):

    s = smservices.objects.get(pk=service_id)
    if s.manage== request.user:

        s.delete() 
        return redirect('services')
    else:
         messages.error(request,("delete is restricted due to different user"))



def profile(request):
    context = {'profile_text': "welcomeaa to profile",
                }
    return render(request,'profile.html',context)

def contact(request):
    context = {'contact_text': "welcome to contact",
                }
    return render(request,'contact.html',context)

def about(request):
    context = {'about_text': "welcome to about",
                }
    return render(request,'about.html',context)    

def index(request):
    context = {'index_text': "INDEx",
                }
    return render(request,'index.html',context)  