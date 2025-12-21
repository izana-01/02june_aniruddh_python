from django.shortcuts import render

# Create your views here.
i=0
def index(request):
    global i
    i+=1 
    return render(request, 'index.html' , {'number': i})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')