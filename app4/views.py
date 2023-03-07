from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f(request):
    return HttpResponse('<h1><marquee>We are Power Star Fans</marquee></h1>')

def g(request):
    return HttpResponse('<h1><marquee>Pawanism!!!!!!!!!!!</marquee></h1>')