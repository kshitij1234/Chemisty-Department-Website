from django.shortcuts import render
from .models import Faculty, Staff, Lab

def directory(request):
    faculty = Faculty.objects.all().order_by("name")
    staff = Staff.objects.all().order_by("name")
    lab = Lab.objects.all().order_by("name")
    object_list = {'faculty': faculty, 'staff': staff, 'lab': lab}
    return render(request, 'directory.html', object_list)
