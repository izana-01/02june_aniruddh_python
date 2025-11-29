from django.shortcuts import render , redirect
from .forms import RegistrationForm

# Create your views here.

def register_view(request):
    form = RegistrationForm()
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            request.session["name"] = form.cleaned_data["full_name"]
            return redirect("success")

    return render(request, "register.html", {"form": form})

def success_view(request):
    name = request.session.get("name", "Guest")
    return render(request, "success.html", {"name": name})
