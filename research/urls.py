from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^areas/$', views.areas, name='areas'),
]
