from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio', views.Portfolio, name="portfolio"),
    path('portfolio/<slug:category>', views.Portfolio),
    path('portfolio/<slug:category>/<slug:group>', views.Portfolio),
]