from django.http import HttpResponse
from django.shortcuts import render


def fridge(request):
    return HttpResponse('<h1>Страница холодильников</h1>')