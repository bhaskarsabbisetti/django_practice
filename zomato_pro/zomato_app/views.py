from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manchuria(req):
    return HttpResponse("manchuria is ready")

def biryani(req):
    return HttpResponse("biryani is ready")