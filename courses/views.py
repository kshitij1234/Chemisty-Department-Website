from django.shortcuts import render
from .models import BtechCourses

def btech_courses(request):
    btech_courses = BtechCourses.objects.all().order_by("id")
    return render(request, 'btech_courses.html', {'btech_courses' : btech_courses})

def msc_courses(request):
    return render(request, 'error_404.html')

def phd_courses(request):
    return render(request, 'error_404.html')
