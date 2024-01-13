from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requesrs -> response
# request handler
# action 

def say_hello(request):
    #pull data from db 
    # transform data 
    return HttpResponse("Hello World")


