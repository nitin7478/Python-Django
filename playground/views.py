from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# requesrs -> response
# request handler
# action 

def calclulate():
    x =1 
    y = 2
    return x


def say_hello(request):
    #pull data from db 
    # transform data 
    x = calclulate()
    return render(request , 'hello.html' , {'name': 'nitin'})




