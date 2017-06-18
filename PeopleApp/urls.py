from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^faculty/$', views.faculty_list, name='faculty_list'),
    url(r'^staff/$', views.staff_list, name='staff_list'),
]
