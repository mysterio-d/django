from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('booking/', views.booking,name='booking'),
    path('doctors/', views.doctors,name='doctors'),
    path('contact', views.contact,name='contact'),
    path('department', views.department,name='department'),
]
