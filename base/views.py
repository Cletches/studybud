from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def connect(request):
    return render(request, 'connect.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')



# Create your views here.
