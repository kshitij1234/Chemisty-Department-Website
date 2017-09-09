from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?i)faculty/*$', views.faculty_list, name='faculty_list'),
    url(r'^(?i)faculty/(?P<pk>.+)$', views.individual_profile, name="individual_profile.html"),
    url(r'^(?i)staff/*$', views.staff_list, name='staff_list'),
    url(r'^(?i)students/UG/*$', views.undergraduate_list, name="undergraduate_list"),
    url(r'^(?i)students/Msc/*$', views.msc_list, name="msc_list"),
    url(r'^(?i)students/Phd/*$', views.phd_list, name='phd_list'),
    url(r'^(?i)students/PhdAlumni/*$', views.phd_alumni_list, name='phd_alumni_list'),
]
