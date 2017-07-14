from django.contrib import admin
from .models import BtechCourses, MscCourses, PhdCourses

admin.site.register(BtechCourses, verbose_name_plural="BtechCourses")
admin.site.register(MscCourses, verbose_name_plural="MscCourses")
admin.site.register(PhdCourses, verbose_name_plural="PhdCourses")
