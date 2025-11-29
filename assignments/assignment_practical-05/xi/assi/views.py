from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # refresh page to show new doctor
    else:
        form = DoctorForm()

    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'form': form, 'doctors': doctors})
