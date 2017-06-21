from django.contrib import admin
from .models import Designations, Batch
from .models import Faculty, Staff, UndergraduateStudents, MscStudents

# Register your models here.

admin.site.register(Designations)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Batch)
admin.site.register(UndergraduateStudents)
admin.site.register(MscStudents)
