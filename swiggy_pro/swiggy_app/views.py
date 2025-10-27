from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biryani(req):
    return HttpResponse("biryani is ready")
def noodiles(req):
    return HttpResponse("noodiles is ready")