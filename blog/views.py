from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Vaasu Garg',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 7, 2023'
    },
    {
        'author': 'Mihika',
        'title': 'Blog Post 3 ',
        'content': 'Third post content',
        'date_posted': 'August 28, 2018'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'learning curve'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1>About me</h1>')
    
