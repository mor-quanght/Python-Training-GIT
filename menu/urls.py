
from django.contrib import admin
from django.urls import path,include
from menu import views



urlpatterns = [
    path('', views.my_menu,name='menu'),

]
