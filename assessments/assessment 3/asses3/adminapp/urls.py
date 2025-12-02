from django.urls import path
from . import views

urlpatterns = [

    path('', views.alogin, name='alogin'),
    path('dashboard/', views.dashboard, name='dashboard'),

    
]