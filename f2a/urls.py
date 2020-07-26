from django.contrib import admin
from django.urls import path, include
from smpool_app import views as services_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', services_views.index),
    path('', include('smpool_app.urls')),
    path('', include('users_app.urls')),
    path('contact.html', services_views.contact, name='contact'),
    path('about.html', services_views.about, name='about'),

    path('career.html', services_views.career, name='career'),
    path('marquee.html', services_views.marquee, name='marquee'),
    path('ccna.html', services_views.ccna, name='ccna'),
    path('cdcs.html', services_views.cdcs, name='cdcs'),
    path('certificate_awards.html', services_views.certificate_awards, name='certificate_awards'),
    path('cisa.html', services_views.cisa, name='cisa'),
    path('clients.html', services_views.clients, name='clients'),
    path('contacts', services_views.contact, name='contacts'),
    path('corporate_profile.html', services_views.corporate_profile, name='corporate_profile'),
    path('directors.html', services_views.directors, name='directors'),
    path('frelancer.html', services_views.frelancer, name='frelancer'),
    path('gallery.html', services_views.gallery, name='gallery'),
    path('ged.html', services_views.ged, name='ged'),
    path('goals.html', services_views.goals, name='goals'),
    path('business_focus.html', services_views.business_focus, name='business_focus'),
    path('hrms.html', services_views.hrms, name='hrms'),
    path('industrial_training.html', services_views.industrial_training, name='industrial_training'),
    path('javase8.html', services_views.javase8, name='javase8'),

    path('lms.html', services_views.lms, name='lms'),
    path('mcse.html', services_views.mcse, name='mcse'),
    path('oracle.html', services_views.oracle, name='oracle'),
    path('pearsonvue.html', services_views.pearsonvue, name='pearsonvue'),
    path('hrms.html', services_views.hrms, name='hrms'),
    path('pms.html', services_views.pms, name='pms'),
    path('pte.html', services_views.pte, name='pte'),
    
    path('redhat.html', services_views.redhat, name='redhat'),
    path('rhcss.html', services_views.rhcss, name='rhcss'),
  
    path('testing_redhat.html', services_views.testing_redhat, name='testing_redhat'),
    path('chatpop.html', services_views.chatpop, name='chatpop'),
    path('toefl.html', services_views.toefl, name='toefl'),
    path('usajob.html', services_views.usajob, name='usajob'),
    path('web_development.html', services_views.web_development, name='web_development'),




]
