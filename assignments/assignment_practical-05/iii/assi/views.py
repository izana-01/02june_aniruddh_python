from django.shortcuts import render
from .forms import PatientForm

# Create your views here.

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {'form': PatientForm(), 'success': True})
    else:
        form = PatientForm()
    return render(request, 'register.html', {'form': form})
