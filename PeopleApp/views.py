from django.shortcuts import render
from .models import Faculty, Staff, UndergraduateStudents, MscStudents, PhdStudents


# Create your views here.

def faculty_list(request):
    faculty = Faculty.objects.all().order_by('name')
    return render(request, 'PeopleApp/FacultyList.html', {'faculty': faculty})


def staff_list(request):
    staff = Staff.objects.all().order_by('name')
    return render(request, 'PeopleApp/StaffList.html', {'staff': staff})


def undergraduate_list(request):
    students13 = UndergraduateStudents.objects.filter(batch__batch__contains="2013").order_by('rollno')
    students14 = UndergraduateStudents.objects.filter(batch__batch__contains="2014").order_by('rollno')
    students15 = UndergraduateStudents.objects.filter(batch__batch__contains="2015").order_by('rollno')
    students16 = UndergraduateStudents.objects.filter(batch__batch__contains="2016").order_by('rollno')
    return render(request, 'PeopleApp/UndergraduateList.html', {'students13': students13,
                                                                'students14': students14,
                                                                'students15': students15,
                                                                'students16': students16})


def msc_list(request):
    students16 = MscStudents.objects.filter(batch__batch__contains="2016").order_by('rollno')
    return render(request, 'PeopleApp/MscList.html', {'students16': students16})

def phd_list(request):
    students17 = PhdStudents.objects.filter(batch__batch__contains="2017")
