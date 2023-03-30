# loginpage/loginpage/urls.py
from django.contrib import admin
from webpage.views import *
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accountss/', include('django.contrib.auth.urls')),
    path('home/', HomeView, name='home'),
    path('register/', register, name='register')
]
