from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?i)projects/$', views.projects, name='projects'),
    url(r'^(?i)areas/$', views.areas, name='areas'),
    url(r'^(?i)publications/$', views.publications, name='publications'),
]
