from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def b(request):
    return HttpResponse('<h1><marquee>Jai Pawan Kalyan</marquee></h1>')

def c(request):
    return HttpResponse('<h1><marquee>Jai Power Star Pawan Kalyan</marquee></h1>')