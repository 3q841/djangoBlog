from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here. ORM - object orented Matadate / sqllite3
posts = [
    {
        'author': 'Eqbal amini',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'may 28, 2020'
    },
    {
        'author': 'Eqbal amini',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': 'may 28, 2020'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
    