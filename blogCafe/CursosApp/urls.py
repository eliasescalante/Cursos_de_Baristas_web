from django.contrib import admin
from django.urls import path
from CursosApp import views

urlpatterns = [
    path('', views.inicio ,name="Inicio"),
]