from django.contrib import admin
from django.urls import path,include
from data import views


urlpatterns = [
    path('second/registerform/Detail/',views.alldetail,name='alldetail'),
]
