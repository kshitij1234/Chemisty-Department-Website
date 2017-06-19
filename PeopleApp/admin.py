from django.contrib import admin
from .models import Designations
from .models import Faculty,Staff
# Register your models here.

admin.site.register(Designations)
admin.site.register(Faculty)
admin.site.register(Staff)