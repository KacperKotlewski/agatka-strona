from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Portfolio, name="portfolio"),
    path('/cat_<slug:category>', views.Portfolio),
    path('/cat_<slug:category>/<int:group>', views.Portfolio),
    path('/cat_<slug:category>/<int:group>/<int:image>', views.Portfolio),
    path('/<int:group>', views.Portfolio),
    path('/<int:group>/<int:image>', views.Portfolio),
    path('/get-subcategories', views.GetSubcategories),
]