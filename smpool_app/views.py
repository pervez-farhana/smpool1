from django.shortcuts import render, redirect
from django.http import HttpResponse
from smpool_app.models import content_service
from django.views import generic 
from smpool_app.models import website_content_info
from smpool_app.models import menu_info
from smpool_app.models import course_info
from smpool_app.models import class_info
from smpool_app.models import course_exam_info
from smpool_app.forms import serviceform
from django.contrib import messages
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required

# Create your views here.
# class view form better than def
class create_search(generic.CreateView ):

    model= content_service
    fields=['service_desc','service_cost']
    template_name='services.html'
    success_url='index.html'

def azax_call(request):
    search_form = searchForm(rquest.GET)
    if search_form.is_valid():
        encoded_search_term= urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=40&q={ encoded_search_term }&key=[YOUTUBE_API_KEY]')
        
        return JsonResponse(response.json())
    return JsonResponse({'error':'not able to validate'})
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
        all_services = content_service.objects.filter(manage=request.user)
        paginator = Paginator(all_services,5)
        page=request.GET.get('pg')
        all_services= paginator.get_page(page)
        return render(request,'services.html',{'all_services': all_services})

def edit_services(request,service_id):
    if request.method == "POST":

        sid = content_service.objects.get(pk=service_id)
        form = serviceform(request.POST or None, instance = sid)
        if form.is_valid():
            form.save()
            messages.success(request,("entry Edited!"))
        else:
            messages.error(request,("error in Entry"))
           
        return redirect('services')
    
    
    else:
    
        service_obj = content_service.objects.get(pk=service_id)
        return render(request,'edit.html',{'service_obj': service_obj})


def delete_service(request, service_id):

    s = content_service.objects.get(pk=service_id)
    if s.manage== request.user:

        s.delete() 
        return redirect('services')
    else:
         messages.error(request,("delete is restricted due to different user"))


#def content_setup(request):
 #   context = {'slide1_text': "Swimming pool company3333333333333333333",
  #              }
  #  return render(request,'contact.html',context)
     

def profile(request):
    career_text
    return render(request,'profile.html',context)
################## contacts #########################

def contact(request):
    context = {'slide1_text': "Swimming to contact",
                }
    
    contacttext =website_content_info.objects.filter(body_pos = 'c1')
    for ccon in contacttext:
        contact_text=ccon.body_area
        contact_title=ccon.body_title
        context['contact_text']= contact_text
        context['contact_title']= contact_title

    ctext2 =website_content_info.objects.filter(body_pos = 'c2')
    for ccon in ctext2:
        contact_text2=ccon.body_area
        contact_title2=ccon.body_title
        context['contact_text2']= contact_text2
        context['contact_title2']= contact_title2
    
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'contact.html',context)


################## CCNA #########################

def ccna(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'ccna')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'ccna.html',context)

#####################MCSE########################
    
def mcse(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'mcse')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'mcse.html',context)
#####################MCSE########################
def web_development(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'web_development')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'web_development.html',context)
#####################usajob########################
def usajob(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'usajob')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'usajob.html',context)
    
#####################toefl########################
def toefl(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'toefl')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'toefl.html',context)
#####################testing_redhat########################
def testing_redhat(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'testing_redhat')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'testing_redhat.html',context)
#####################rhcss########################

def rhcss(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'rhcss')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'rhcss.html',context)
#####################redhat########################

def redhat(request):
    context = {'slide1_text': "Swimming to contact",  }
    rh= website_content_info.objects.filter(body_pos__contains = 'redhat')
    
    for crh in rh:
        bda =crh.body_area
        bid=crh.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['rh']=   rh
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'redhat.html',context)

#####################chat########################

def chatpop(request):
    context = {'slide1_text': "Swimming to contact",
                }
    chatpop= website_content_info.objects.filter(body_pos__contains = 'chatpop')
    context['chatpop']=   chatpop

        
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'chatpop.html',context)
#####################pte########################


def pte(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'pte')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'pte.html',context)
#####################pms########################

def pms(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'pms')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'pms.html',context)

#####################pearsonvue########################
def pearsonvue(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'pearsonvue')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'pearsonvue.html',context)
#####################oracle########################

def oracle(request):

    context = {'slide1_text': "Swimming to contact",  }
    rh= website_content_info.objects.filter(body_pos__contains = 'oracle')
    
    for crh in rh:
        bda =crh.body_page
        bid=crh.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        
        elif bda == "course":
            ocourse =course_info.objects.filter(bodyid_id = bid)
            context['ocourse']=   ocourse
        
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['rh']=   rh
    
    
    ocourse =course_info.objects.filter(course_code = 'How can be a good DBA?')
    context['ocourse']=   ocourse
        
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'oracle.html',context)
#####################lms########################
def lms(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'lms')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'lms.html',context)

#####################javase8########################
def javase8(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'javase8')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'javase8.html',context)


#####################industrial_training########################

def industrial_training(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'industrial_training')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'industrial_training.html',context)
#####################hrms########################

def hrms(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'hrms')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'hrms.html',context)

#####################goals########################

def goals(request):
    context = {'slide1_text': "Swimming to contact",  }
    gls= website_content_info.objects.filter(body_pos__contains = 'goals')
    
    for cgls in gls:
        bda =cgls.body_area
        bid=cgls.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['gls']=   gls
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'goals.html',context)
#####################gmat########################

def gmat(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'gmat')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'gmat.html',context)

#####################frelancer########################

def frelancer(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'frelancer')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'frelancer.html',context)

#####################directors########################
def directors(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'directors')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'directors.html',context)

#####################corporate_profile########################


def corporate_profile(request):
    context = {'slide1_text': "Swimming to contact",  }
    corp= website_content_info.objects.filter(body_pos__contains = 'corporate_profile')
    
    for ccorp in corp:
        bda =ccorp.body_area
        bid=ccorp.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['corp']=   corp
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'corporate_profile.html',context)

#####################clients########################
def clients(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'clients')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'clients.html',context)

#####################ged########################
def ged(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'ged')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'ged.html',context)
#####################cisa#############################################MCSE########################
def cisa(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'cisa')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'cisa.html',context)



#####################certificate_awards#############################################MCSE########################

def certificate_awards(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'certificate_awards')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'certificate_awards.html',context)
    
    
    #####################ceh########################

def ceh(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'ceh')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'ceh.html',context)
    
    
    #####################MCcdcsSE########################

def cdcs(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'cdcs')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'cdcs.html',context)



#####################career########################

def career(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'career')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'career.html',context)

#####################career########################

def gallery(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'gallery')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'gallery.html',context)



#####################business_focus########################

def business_focus(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'business_focus')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'business_focus.html',context)

    #####################bcat########################

def bcat(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'bcat')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'bcat.html',context)

    #####################aspnet########################

def aspnet(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'aspnet')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'aspnet.html',context)

 #####################ams########################

def ams(request):
    context = {'slide1_text': "Swimming to contact",  }
    bzf= website_content_info.objects.filter(body_pos__contains = 'ams')
    
    for cbzf in bzf:
        bda =cbzf.body_area
        bid=cbzf.id
       
        if bda == "course1":
            redhatcourse1 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse1']=   redhatcourse1
        elif bda == "course2":
            redhatcourse2 =course_info.objects.filter(bodyid_id = bid)
            context['redhatcourse2']=   redhatcourse2
        
        elif bda == "class1":
            
            redhatclass1 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass1']=   redhatclass1
        elif bda == "class2":
            
            redhatclass2 =class_info.objects.filter(bodyid_id = bid)
            context['redhatclass2']=   redhatclass2
        elif bda == "exam1":
            
            redhatexam1 =course_exam_info.objects.filter(bodyid_id = bid)
            context['redhatexam1']=   redhatexam1
        
        else:
            context['bzf']=   bzf
            
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu

    return render(request,'ams.html',context)

#####################others########################
def marquee(request):
    context = {'about_text': "welcome to about",
                }
    return render(request,'marquee.html',context) 

def about(request):
    context = {'about_text': "welcome to about",
                }
    return render(request,'about.html',context)    

def index(request):
    context = {'slide1_text': "Swimming to contact",
                }
    slider =website_content_info.objects.filter(body_pos__contains = 'slider_text')
    for objcon in slider:
        slider_title=objcon.body_title
        slider_subtitle=objcon.body_subtitle
        slider_text=objcon.body_text
        if objcon.body_pos =="slider_text1":

            context = {'body_text1': slider_text,
                'title_text1' : slider_title,
                'subtitle_text1' :slider_subtitle
                }
        elif objcon.body_pos =="slider_text2":
            context['body_text2']= slider_text
            context['title_text2'] = slider_title
            context['subtitle_text2'] =slider_subtitle
        
        elif objcon.body_pos =="slider_text3":
            context['body_text3']= slider_text
            context['title_text3'] = slider_title
            context['subtitle_text3'] =slider_subtitle

    wtext =website_content_info.objects.filter(body_pos = 'w1')
    for wcon in wtext:
        welcome_title=wcon.body_title
        welcome_text=wcon.body_text
        context['welcome_title']= welcome_title
        context['welcome_text']= welcome_text
    cptext =website_content_info.objects.filter(body_pos = 'aboutus_text')
    for ccon in cptext:
        aboutus_text=ccon.body_area
        context['aboutus_text']= aboutus_text
    nwstext =website_content_info.objects.filter(body_pos = 'news1')
    for ccon in nwstext:
        news_text=ccon.body_text
        news_title=ccon.body_title
        context['news_text']= news_text
        context['news_title']= news_title
        
    nwstext2 =website_content_info.objects.filter(body_pos = 'news2')
    for ccon in nwstext2:
        news_text2=ccon.body_text
        news_title2=ccon.body_subtitle
        context['news_text2']= news_text2
        context['news_title2']= news_title2
    
    nwstext3 =website_content_info.objects.filter(body_pos = 'news3')
    for ccon in nwstext3:
        news_text3=ccon.body_text
        news_title3=ccon.body_subtitle
        context['news_text3']= news_text3
        context['news_title3']= news_title3
    
    tamenu = menu_info.objects.filter(menu_name__contains = 'Training Academy')
    context['tamenu']=   tamenu

    tcmenu = menu_info.objects.filter(menu_name__contains = 'Testing Center')
    context['tcmenu']=   tcmenu

    smenu = menu_info.objects.filter(menu_name__contains = 'Software')
    context['smenu']=   smenu
    scmenu = menu_info.objects.filter(menu_name__contains = 'Secuirty Course')
    context['scmenu']=   scmenu

    jpmenu = menu_info.objects.filter(menu_name__contains = 'Job Placement')
    context['jpmenu']=   jpmenu
    aumenu = menu_info.objects.filter(menu_name__contains = 'About US')
    context['aumenu']=   aumenu
    
    return render(request,'index.html',context) 
   