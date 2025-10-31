from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(req):
    return HttpResponse("hello user good to see you")
