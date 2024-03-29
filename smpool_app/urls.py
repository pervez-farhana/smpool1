from django.urls import path
from smpool_app import views

urlpatterns = [
    path('', views.index, name='profile'),
    path('services/delete/<service_id>', views.delete_service, name='delete_service'),
    path('services/edit/<service_id>', views.edit_services, name='edit_services'),

    path('services', views.sservices, name='services'),
    path('ssearch', views.create_search, name='ssearch'),
]
