from django.contrib import admin
from django.urls import path, include
from smpool_app import views as services_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', services_views.index),
    path('', include('smpool_app.urls')),
    path('', include('users_app.urls')),
    path('contact', services_views.contact, name='contact'),
    path('about', services_views.about, name='about'),
]
