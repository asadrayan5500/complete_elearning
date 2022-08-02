from unicodedata import name
from django.contrib import admin
from django.urls import path
from learn_online import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('our experts', views.team, name='team'),
    path('contact', views.contact, name= 'contact')
]
