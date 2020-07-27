from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Portfolio, name="portfolio"),
    path('/<slug:category>', views.Portfolio),
    path('/<slug:category>/<slug:group>', views.Portfolio),
    path('/get-subcategories', views.GetSubcategories),
]