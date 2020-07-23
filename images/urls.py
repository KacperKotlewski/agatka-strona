from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:image>', views.Images),
    path('<slug:group>/<slug:image>', views.Images),
    path('<slug:category>/<slug:group>/<slug:image>', views.Images),
]