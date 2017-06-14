from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^faculty/$', views.faculty_list, name='faculty_list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)