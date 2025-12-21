from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'cover_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
