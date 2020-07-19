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
    path('ccna.html', services_views.about, name='ccna'),
    path('cdcs.html', services_views.contact, name='cdcs'),
    path('certificate_awards.html', services_views.about, name='certificate_awards'),
    path('cisa.html', services_views.cisa, name='cisa'),
    path('clients.html', services_views.about, name='clients'),
    path('contacts', services_views.contact, name='contacts'),
    path('corporate_profile.html', services_views.about, name='corporate_profile'),
    path('directors.html', services_views.contact, name='directors'),
    path('frelancer.html', services_views.about, name='frelancer'),
    path('gallery.html', services_views.contact, name='gallery'),
    path('ged.html', services_views.about, name='ged'),
    path('goals.html', services_views.contact, name='goals'),
    path('hrms.html', services_views.about, name='hrms'),
    path('industrial_training.html', services_views.contact, name='industrial_training'),
    path('javase8.html', services_views.about, name='javase8'),

    path('lms.html', services_views.about, name='lms'),
    path('mcse.html', services_views.contact, name='mcse'),
    path('oracle.html', services_views.oracle, name='oracle'),
    path('pearsonvue.html', services_views.contact, name='pearsonvue'),
    path('hrms.html', services_views.about, name='hrms'),
    path('pms.html', services_views.contact, name='pms'),
    path('pte.html', services_views.about, name='pte'),
    
    path('redhat.html', services_views.redhat, name='redhat'),
    path('rhcss.html', services_views.contact, name='rhcss'),
    path('oracle.html', services_views.about, name='oracle'),
    path('testing_redhat.html', services_views.contact, name='testing_redhat'),
    path('chatpop.html', services_views.chatpop, name='chatpop'),
    path('toefl.html', services_views.about, name='toefl'),
    path('usajob.html', services_views.contact, name='usajob'),
    path('web_development.html', services_views.about, name='web_development'),




]
