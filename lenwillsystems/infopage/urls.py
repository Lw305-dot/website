from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('maintenance',views.maintenance,name='maintenance'),
    path('modification',views.Modification,name='modification'),
    path('installation',views.installation,name='installation'),
    path('spareparts',views.spareparts,name='spareparts'),
    path('materialhandling',views.materialhandling,name='materialhandling')
]
    

   
    
