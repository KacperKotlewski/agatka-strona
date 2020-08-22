from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('home', views.Homepage, name="homepage"),
    path('home/<int:group>', views.Homepage, name="homepage"),
    path('home/<int:group>/<int:image>', views.Homepage, name="homepage"),
    path('SetDarkMode', views.SetDarkMode, name="SetDarkMode"),
    path('messeges', views.Messeges, name="Messeges"),
]