from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Alpha/home.html')


def about(request):
    return render(request, 'Alpha/about.html')

def repo(request):
	return render(request, 'Alpha/repo.html')

def cv(request):
	return render(request, 'Alpha/cv.html')