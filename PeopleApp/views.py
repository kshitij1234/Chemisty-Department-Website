from django.shortcuts import render
from .models import Faculty, Staff, UndergraduateStudents, MscStudents, PhdStudents, PhdAlumni

def individual_profile(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return render(request, 'error_404.html')
    return render(request, 'PeopleApp/individual_profile.html', {'faculty':faculty})

def faculty_list(request):
    faculty = Faculty.objects.all().order_by('list_position')
    return render(request, 'PeopleApp/FacultyList.html', {'faculty': faculty})


def staff_list(request):
    staff = Staff.objects.all().order_by('name')
    return render(request, 'PeopleApp/StaffList.html', {'staff': staff})


def undergraduate_list(request):
    students13 = UndergraduateStudents.objects.filter(batch__batch__contains="2013").order_by('rollno')
    students14 = UndergraduateStudents.objects.filter(batch__batch__contains="2014").order_by('rollno')
    students15 = UndergraduateStudents.objects.filter(batch__batch__contains="2015").order_by('rollno')
    students16 = UndergraduateStudents.objects.filter(batch__batch__contains="2016").order_by('rollno')
    students17 = UndergraduateStudents.objects.filter(batch__batch__contains="2017").order_by('rollno')
    students18 = UndergraduateStudents.objects.filter(batch__batch__contains="2018").order_by('rollno')
    students19 = UndergraduateStudents.objects.filter(batch__batch__contains="2019").order_by('rollno')
    students20 = UndergraduateStudents.objects.filter(batch__batch__contains="2020").order_by('rollno')
    return render(request, 'PeopleApp/UndergraduateList.html', {'students13': students13,
                                                                'students14': students14,
                                                                'students15': students15,
                                                                'students16': students16,
                                                                'students17': students17,
                                                                'students18': students18,
                                                                'students19': students19,
                                                                'students20': students20,
                                                                })


def msc_list(request):
    students16 = MscStudents.objects.filter(batch__batch__contains="2016").order_by('rollno')
    students17 = MscStudents.objects.filter(batch__batch__contains="2017").order_by('rollno')
    students18 = MscStudents.objects.filter(batch__batch__contains="2018").order_by('rollno')
    students19 = MscStudents.objects.filter(batch__batch__contains="2019").order_by('rollno')
    students20 = MscStudents.objects.filter(batch__batch__contains="2020").order_by('rollno')
    return render(request, 'PeopleApp/MscList.html', {'students16': students16,
                                                      'students17': students17,
                                                      'students18': students18,
                                                      'students19': students19,
                                                      'students20': students20,
                                                      })


def phd_list(request):
    students20 = PhdStudents.objects.filter(batch__batch__contains="2020").order_by('name')
    students19 = PhdStudents.objects.filter(batch__batch__contains="2019").order_by('name')
    students18 = PhdStudents.objects.filter(batch__batch__contains="2018").order_by('name')
    students17 = PhdStudents.objects.filter(batch__batch__contains="2017").order_by('name')
    students16 = PhdStudents.objects.filter(batch__batch__contains="2016").order_by('name')
    students15 = PhdStudents.objects.filter(batch__batch__contains="2015").order_by('name')
    students14 = PhdStudents.objects.filter(batch__batch__contains="2014").order_by('name')
    students13 = PhdStudents.objects.filter(batch__batch__contains="2013").order_by('name')
    students11 = PhdStudents.objects.filter(batch__batch__contains="2011").order_by('name')
    students10 = PhdStudents.objects.filter(batch__batch__contains="2010").order_by('name')
    students9 = PhdStudents.objects.filter(batch__batch__contains="2009").order_by('name')
    return render(request, 'PeopleApp/PhdList.html', {'students17': students17,
                                                      'students16': students16,
                                                      'students15': students15,
                                                      'students14': students14,
                                                      'students13': students13,
                                                      'students11': students11,
                                                      'students10': students10,
                                                      'students9': students9,
                                                      'students18': students18,
                                                      'students19': students19,
                                                      'students20': students20,
                                                      })


def phd_alumni_list(request):
    alumni = PhdAlumni.objects.all().order_by('name')
    return render(request, 'PeopleApp/PhdAlumniList.html', {'alumni': alumni})
