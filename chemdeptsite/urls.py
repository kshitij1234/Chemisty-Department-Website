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
from . import views

urlpatterns = [
    url(r'^(?i)admin/', admin.site.urls),
    url(r'^(?i)$', views.index, name="home"),
    url(r'^(?i)news/*$', views.news, name="news"),
    url(r'^(?i)news/(?P<pk>\d+)$', views.individual_news, name="individual_news.html"),
    url(r'^(?i)admissions/postgraduate/*$', views.admissions_postgraduate, name="postgraduate_admissions"),
    url(r'^(?i)admissions/doctoral/*$', views.admissions_doctoral, name="doctoral_admissions"),
    url(r'^(?i)admissions/FAQ/*$', views.admissions_faq, name="faq_admissions"),
    url(r'^(?i)sitemap/*$', views.sitemap, name="sitemap"),
    url(r'^(?i)head-message/*$', views.head_msg, name="head_msg"),
    url(r'^(?i)head-profile/*$', views.head_profile, name="head_profile"),
    url(r'^(?i)facilities/*$', views.facilities, name="facilities"),
    url(r'^(?i)directory/*', include('directory.urls')),
    url(r'^(?i)people/', include('PeopleApp.urls')),
    url(r'^(?i)events/*', include('Events.urls')),
    url(r'^(?i)research/', include('research.urls')),
    url(r'^(?i)academics/', include('courses.urls')),


    # please keep this url at the end, this needs to be last in the list
    url(r'^', views.error_404, name="error_404"),
]
