from django.contrib import admin
from .models import Projects,ResearchAreas, CurrentResearch

admin.site.register(Projects, verbose_name_plural="Projects")
admin.site.register(ResearchAreas, verbose_name_plural="Research Areas")
admin.site.register(CurrentResearch, verbose_name_plural="Current Research")
