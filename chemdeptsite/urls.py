"""chemdeptsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import DetailView
from .models import News
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^news/$', views.news, name="news"),
    url(r'^news/(?P<pk>\d+)$', DetailView.as_view(model=News, template_name="new_individual.html")),
    url(r'^sitemap/$', views.sitemap, name="sitemap"),
    url(r'^head-message/$', views.head_msg, name="head_msg"),
    url(r'^facilities/$', views.facilities, name="facilities"),
    url(r'^directory/', include('directory.urls')),
    url(r'^people/', include('PeopleApp.urls')),
    url(r'^events/', include('Events.urls')),
    url(r'^research/', include('research.urls')),

    # please keep this url at the end, this needs to be last in the list
    url(r'^', views.error_404, name="error_404"),
]
