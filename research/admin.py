from django.contrib import admin
from .models import Projects

admin.site.register(Projects, verbose_name_plural="Projects")
