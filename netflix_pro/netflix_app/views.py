from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kantara(req):
    return HttpResponse("kantara movie is playing")
def bahubali(req):
    return HttpResponse("bahubali movie is playing")
def pushpa(req):
    return HttpResponse("pushpa movie is playing")
