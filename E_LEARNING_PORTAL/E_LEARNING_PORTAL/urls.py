"""E_LEARNING_PORTAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from UIC_LEARNING.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', About, name='About'),
    path('Efront/', Efront,  name='Efront'),
    path('htmlCourse/', htmlCourse,  name='htmlCourse'),
    path('enrollForm/', enrollForm,  name='enrollForm'),
    path('enrollFormAPI/', enrollFormAPI,  name='enrollFormAPI'),
    path('pythonCourse/', pythonCourse ,  name='pythonCourse'),
    path('javaCourse/', javaCourse,  name='javaCourse'),
    path('LoginForm/', LoginForm,  name='LoginForm'),
    path('LoginFormAPI/', LoginFormAPI,  name='LoginFormAPI'),
    path('htmlVideo/', htmlVideo,  name='htmlVideo'),
    path('pythonVideo/', pythonVideo,  name='pythonVideo'),
    path('javaVideo/', javaVideo,  name='javaVideo'),
    
]
