from django.contrib import admin
from .models import NoticeBoard, Events, News, Research, QuickLinks

admin.site.register(NoticeBoard, verbose_name_plural="NoticeBoard")
admin.site.register(Events, verbose_name_plural="Events")
admin.site.register(News, verbose_name_plural="News")
admin.site.register(Research, verbose_name_plural="Research")
admin.site.register(QuickLinks, verbose_name_plural="QuickLinks")