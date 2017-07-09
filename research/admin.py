from django.contrib import admin
from .models import Projects,ResearchAreas

admin.site.register(Projects, verbose_name_plural="Projects")
admin.site.register(ResearchAreas, verbose_name_plural="Research Areas")
