from django.contrib import admin
from .models import Faculty, Staff, Lab

admin.site.register(Faculty, verbose_name_plural="Faculty")
admin.site.register(Staff, verbose_name_plural="Staff")
admin.site.register(Lab, verbose_name_plural="Laboratory & Offices")
