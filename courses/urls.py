from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^btech/$', views.btech_courses, name="btech_courses"),
    url(r'^msc/$', views.msc_courses, name="msc_courses"),
    url(r'^phd/$', views.phd_courses, name="phd_courses"),
]
