from django.shortcuts import render
from .models import Post #import database from models file.

#let's see how gits going
# Create your views here.
def home(request):
    #context dictionary to pass as arguments to html page
    context = {
        'posts': Post.objects.all() #query all post in database
    }
    return render(request, 'blog/home.html', context)


def about(request):
    #pass a dictionary dynamically
    return render(request, 'blog/about.html', {'title': 'About'})
