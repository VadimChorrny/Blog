from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def design(request):
    return render(request, 'main/design.html')

def technologies(request):
    return render(request, 'main/technologies.html')

def travel(request):
    return render(request, 'main/travel.html')
