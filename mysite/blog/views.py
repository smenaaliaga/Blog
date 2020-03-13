from django.shortcuts import render, HttpResponse
from .models import Post 
import datetime

def home(request) :
    posts = Post.objects.all()
    date = datetime.datetime.now()
    return render(request, "blog/home.html", {'posts' : posts, 'date' : date})

def post(request, id) :
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post' : post})

def year_posts(request, year) : 
    posts = Post.objects.all().filter(published_date__year = year)
    return render(request, "blog/year_posts.html", {'posts' : posts, 'year' : year})