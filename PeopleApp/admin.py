from django.contrib import admin
from .models import Designations, Batch
from .models import Faculty, Staff, UndergraduateStudents, MscStudents, PhdStudents, PhdAlumni

# Register your models here.

admin.site.register(Designations, verbose_name_plural="Designations")
admin.site.register(Faculty, verbose_name_plural="Faculty")
admin.site.register(Staff, verbose_name_plural="Staff")
admin.site.register(Batch, verbose_name_plural="Batch")
admin.site.register(UndergraduateStudents, verbose_name_plural="UndergraduateStudents")
admin.site.register(MscStudents, verbose_name_plural="MscStudents")
admin.site.register(PhdStudents, verbose_name_plural="PhdStudents")
admin.site.register(PhdAlumni, verbose_name_plural="PhdAlumni")
