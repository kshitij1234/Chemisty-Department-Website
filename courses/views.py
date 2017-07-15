from django.shortcuts import render
from .models import BtechCourses, MscCourses, PhdCourses

def btech_courses(request):
    btech_courses = BtechCourses.objects.all().order_by("id")
    return render(request, 'btech_courses.html', {'btech_courses' : btech_courses})

def msc_courses(request):
    msc_courses = MscCourses.objects.all().order_by("id")
    return render(request, 'msc_courses.html', {'msc_courses' : msc_courses})

def phd_courses(request):
    phd_courses = PhdCourses.objects.all().order_by("id")
    return render(request, 'phd_courses.html', {'phd_courses' : phd_courses})
