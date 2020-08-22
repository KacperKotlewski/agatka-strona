from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Better_admin, name="better_admin"),
    path('add_images/', views.AddImages),
    path('add_images/get_groups/', views.GetGroups),
    path('add_images/new_group/', views.NewGroup),
    path('add_images/new_image/', views.NewImage),
    path('image_compress_all/', views.CompressAllImages),
    path('image_compress/', views.CompressImages),
    path('panel/', admin.site.urls),
    path('login/', views.Login, name="login"),
]