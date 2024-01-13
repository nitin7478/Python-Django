# Django tutorials

Create virtual environment 
```
    conda create -p venv python -y
```

```
pip install requirements.txt
```

```
django-admin startproject project_name .
```

```
python manage.py runserver
```

```
python manage.py startapp playground
```

register the installed app playground in settings.py file inside project_name folder under INSTALLED_APPS = ['playground']

write functions in playground/views.py file
```
def say_hello(request):
    #pull data from db 
    # transform data 
    return HttpResponse("Hello World")
```

write urls to access those functions in urlpatterns inside in playground/urls.py folder
```
urlpatterns = [
    path('hello/', views.say_hello)
]
```

Add those urls in urlpatterns urls.py folder inside storefront/urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
    
]
```




