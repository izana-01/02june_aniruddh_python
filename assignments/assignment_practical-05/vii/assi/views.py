from django.shortcuts import render, get_object_or_404
from .models import Doctor

# Create your views here.

def list(request):
    doctors = Doctor.objects.all()
    return render(request, "list.html", {"doctors": doctors})

def detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, "details.html", {"doctor": doctor})
