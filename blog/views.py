from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post,Question

# Create your views here. ORM - object orented Matadate / sqllite3

def home(request):

    context = {
        'posts': Post.objects.all(),
        #'questions': Question.objects.all()
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def question(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request, 'blog/question.html', context)
    