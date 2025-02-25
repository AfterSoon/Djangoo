# forms.py
from django import forms
from .models import My_blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = My_blog
        fields = ['title', 'content']