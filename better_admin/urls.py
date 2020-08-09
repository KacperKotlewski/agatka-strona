from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Better_admin, name="better_admin"),
    path('panel/', admin.site.urls),
    path('login/', views.Login, name="login"),
]