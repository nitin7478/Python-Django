from django.urls import path 
from . import views

# this is url configuration 
urlpatterns = [
    path('hello/', views.say_hello)
]