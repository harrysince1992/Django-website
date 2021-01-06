from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'blog/home.html', {'title': 'Homepage'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})