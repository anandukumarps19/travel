from django.contrib import admin
from django.urls import path,include
from . import views

app_name='travelapp'

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
