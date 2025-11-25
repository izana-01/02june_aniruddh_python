from django.shortcuts import render
from .models import *

def doc_list(request):
    doctors = Doctor.objects.all()
    # actual template file is 'doc_list.html' in the app templates
    return render(request, 'doc_list.html', {'doctors': doctors})
