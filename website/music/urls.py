from django.urls import path, re_path
from . import views

app_name='music'

urlpatterns = [
    path('', views.index, name='index'),
   
    re_path(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
    re_path(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='details'),