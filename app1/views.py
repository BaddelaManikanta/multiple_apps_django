from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def m(request):
    return HttpResponse('<h1><marquee>Hi How are you!!!! </marquee></h1>')

def a(request):
    return HttpResponse('<h2><marquee>I am Fine.!!!! And You  </marquee></h2>')

def n(request):
    return HttpResponse('<h2><marquee>I am good !!!</marquee></h2>')

def i(request):
    return HttpResponse('<h2><marquee>Srujana Thinnava raa!!!!!</marquee></h2>')