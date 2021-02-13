"""project1 URL Configuration

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
from django.urls import path,include
from . import views

admin.site.site_header="Indian Medical Webservices Admin Panel"
admin.site.site_title="Indian Medical Webservices Admin Panel.com"
admin.site.index_title="Welcome Doctor,Here,You can search your patients with the help of filters,Searchbox"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first,name='first'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('signup/',views.handlesignup,name='handlesignup'),
    path('second/',views.second,name='second'),
    path('second/login/logout/',views.handlelogout,name='handlelogout'),
    path('second/doctors/',views.doctors,name='doctors'),
    path('second/help/',views.help,name='help'),
    path('second/hospitals/',views.hospitals,name='hospitals'),
    path('second/registerform/',views.registerform,name='registerform'),#
   # path('login/registerform/',views.registerform,name='registerform'),
   # path('login/doctors/',views.doctors,name='doctors'),
    #path('login/hospitals/',views.hospitals,name='hospitals'),
    #path('login/login/logout/',views.handlelogout,name='handlelogout'),
   # path('login/help/',views.help,name='help'),
    path('data/',include('data.urls')),
]
