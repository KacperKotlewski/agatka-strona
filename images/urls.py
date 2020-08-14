from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('/<slug:image>', views.Images),
    # path('/<slug:group>/<slug:image>', views.Images),
    # path('/<slug:category>/<slug:group>/<slug:image>', views.Images),
    path('s_from_groups', views.GetGroups),
    path('s_group_gallery', views.GetGroupGallery),
    path('s', views.GetImages),
]