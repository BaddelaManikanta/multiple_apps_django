from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def k(request):
    return HttpResponse('<h1><marquee>Jai Power Star</marquee></h1>')

def t(request):
    return HttpResponse('<h1><marquee>Jai JanaSena</marquee></h1>')
