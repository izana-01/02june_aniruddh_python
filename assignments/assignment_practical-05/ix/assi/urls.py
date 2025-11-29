from django.urls import path 
from assi import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
]