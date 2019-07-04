from django.shortcuts import render
from .models import Post
from . import chatbot


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def submit(request):
	info = request.POST['input']
	response = chatbot.getResponse(info)
	return render(request, 'blog/home.html', {'response': response})