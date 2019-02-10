from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Alpha/home.html')


def about(request):
    return render(request, 'Alpha/about.html')


def bookone(request):
    return render(request, 'Alpha/bookone.html')


def skyrim(request):
    return render(request, 'Alpha/skyrim.html')
