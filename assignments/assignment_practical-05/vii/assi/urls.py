from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="doctor_list"),
    path('<int:id>/', views.detail, name="doctor_detail"),
]
