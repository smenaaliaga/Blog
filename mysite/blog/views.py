from django.shortcuts import render, HttpResponse
from .models import Post    
import datetime, calendar

def home(request) :
    posts = Post.objects.all()
    date = datetime.datetime.now()
    return render(request, "blog/home.html", {'posts' : posts, 'date' : date})

def year_posts(request, year) : 
    posts = Post.objects.all().filter(published_date__year = year)
    return render(request, "blog/year_posts.html", {'posts' : posts, 'year' : year})

def month_posts(request, year, month) : 
    posts = Post.objects.all().filter(published_date__year = year, published_date__month = month)
    month_name = month_es(month)
    return render(request, "blog/month_posts.html", {'posts' : posts, 'year' : year, 'month' : month, 'month_name' : month_name})

def detail_posts(request, year, month, id) :
    post = Post.objects.get(id = id)
    return render(request, "blog/detail_posts.html", {'post' : post})


# Mandar a clase py especifica
def month_es(month):
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    mes = meses[month - 1]

    return mes