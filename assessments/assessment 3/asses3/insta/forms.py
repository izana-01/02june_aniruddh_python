from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows':3,'placeholder':'Write your caption...'})
        }


class CommentForm(forms.Form):
    name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder':'Your name (optional)'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Write a comment...'}), max_length=2000)
