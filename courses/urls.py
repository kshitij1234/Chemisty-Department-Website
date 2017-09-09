from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?i)btech/*$', views.btech_courses, name="btech_courses"),
    url(r'^(?i)msc/*$', views.msc_courses, name="msc_courses"),
    url(r'^(?i)phd/*$', views.phd_courses, name="phd_courses"),
]
