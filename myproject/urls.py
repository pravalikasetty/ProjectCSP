"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1.views import about,register, doregister,login,logincheck,resume,userhome,adminhome,viewusers,modify,one,doresume
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',about),
    path('register/',register),
    path('doregister/',doregister),
    path('login/',login),
    path('logincheck/',logincheck),
    path('resume/',resume),
    path('userhome/',userhome),
    path('adminhome/',adminhome),
    path('viewusers/',viewusers),
    path('modify/',modify),
    path('one/',one),
    path('doresume/',doresume),

  
    
    
]
