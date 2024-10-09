from django.shortcuts import render
from .models import Post  # Make sure to import your model

def home(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'blog/home.html', {'posts': posts})

