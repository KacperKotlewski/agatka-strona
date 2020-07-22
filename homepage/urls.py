from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('SetDarkMode', views.SetDarkMode, name="SetDarkMode"),
]