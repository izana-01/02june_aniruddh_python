from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment, Follow
from .forms import CommentForm
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def home(request):
    # basic search: if `q` provided, filter by title or content (case-insensitive)
    q = request.GET.get('q', '')
    if q:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, "home.html", {"posts": posts, "q": q})


def post_detail(request, id):
    post = Post.objects.get(id=id)

    # Handle comment submission (allow anonymous comments)
    comments = post.comments.order_by('created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            content = form.cleaned_data.get('content')
            if request.user.is_authenticated:
                Comment.objects.create(user=request.user, post=post, content=content, author_name=request.user.username)
            else:
                Comment.objects.create(user=None, post=post, content=content, author_name=name or 'Anonymous')
            return redirect('insta:post_detail', id=post.id)
    else:
        form = CommentForm()

    # whether current user liked this post
    user_liked = False
    if request.user.is_authenticated:
        user_liked = post.likes.filter(user=request.user).exists()

    context = {
        "post": post,
        "comments": comments,
        "comment_form": form,
        "user_liked": user_liked,
        "like_count": post.likes.count(),
        "author_followers_count": post.user.followers_set.count(),
        "user_follows_author": request.user.is_authenticated and Follow.objects.filter(follower=request.user, following=post.user).exists(),
    }
    return render(request, "post_detail.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('insta:home')

    return render(request, "create_post.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        # Log the new user in immediately and redirect to main page
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('insta:home')
        # Fallback to namespaced login if authentication failed for some reason
        return redirect('insta:login')

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('insta:home')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('insta:login')


@login_required
def like_post(request, id):
    # Toggle like on a post
    post = Post.objects.get(id=id)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect('insta:post_detail', id=post.id)


@login_required
def toggle_follow(request, user_id):
    # Toggle follow/unfollow for the given user_id
    try:
        target = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', reverse('insta:home')))

    # prevent following yourself
    if target == request.user:
        return redirect(request.META.get('HTTP_REFERER', reverse('insta:home')))

    existing = Follow.objects.filter(follower=request.user, following=target)
    if existing.exists():
        existing.delete()
    else:
        Follow.objects.create(follower=request.user, following=target)

    return redirect(request.META.get('HTTP_REFERER', reverse('insta:home')))

