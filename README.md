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
from django.urls import include
urlpatterns = 
[
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
    
]
```

Setup deubug launch.json file
```click on debug on left side and click on launch.json and select Django run configuration in top box.
    It will launch.json file inside .vscode folder
    Change Debug Server to Port 9000 (Your choice)
    Open the file andd change configurations =>  args >  add argumaent "9000" , we are changing default server port


Install django-debug-toolbar
```
pip install django-debug-toolbar
```

Add debug toolbar in list of installed apps inside project_name/settings.py
```
'django.contrib.staticfiles'
"debug_toolbar"
```

Add path inside urlpatters in project_name/urls.py
```
path("__debug__/", include("debug_toolbar.urls")),
```

Add middleware inside project_name/settings.py
```
"debug_toolbar.middleware.DebugToolbarMiddleware"
```

Add below code in same file project_name/settings.py
```
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```






