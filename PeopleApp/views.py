from django.shortcuts import render
from .models import Faculty,Staff
# Create your views here.

def faculty_list(request):
    faculty = Faculty.objects.all().order_by('name')
    return render(request, 'PeopleApp/FacultyList.html', {'faculty': faculty})

def staff_list(request):
    staff = Staff.objects.all().order_by('name')
    return render(request, 'PeopleApp/StaffList.html', {'staff': staff})