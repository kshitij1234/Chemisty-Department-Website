from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^faculty/$', views.faculty_list, name='faculty_list'),
    url(r'^staff/$', views.staff_list, name='staff_list'),
    url(r'^students/UG$', views.undergraduate_list, name="undergraduate_list"),
    url(r'^students/Msc$', views.msc_list, name="msc_list"),
    url(r'^students/Phd$', views.phd_list, name='phd_list'),
]
