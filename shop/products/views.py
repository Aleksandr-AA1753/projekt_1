from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Главная страница</h1>')

def fridge(request):
    return HttpResponse('<h1>Страница холодильников</h1>')