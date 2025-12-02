from django.shortcuts import render , redirect
from insta.models import Post

# Create your views here.

def dashboard(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "dashboard.html", {"posts": posts})

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def alogin(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect("dashboard")
        else:
            error = "Invalid username or password"

    return render(request, "alogin.html", {"error": error})
