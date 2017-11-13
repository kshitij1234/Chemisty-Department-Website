from django.contrib import admin
from .models import NoticeBoard, News, QuickLinks, HeadsDesk, Facilities

admin.site.register(NoticeBoard, verbose_name_plural="NoticeBoard")
admin.site.register(News, verbose_name_plural="News")
admin.site.register(QuickLinks, verbose_name_plural="QuickLinks")
admin.site.register(HeadsDesk, verbose_name_plural="HeadsDesk")
admin.site.register(Facilities, verbose_name_plural="Facilities")
