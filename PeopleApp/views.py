from django.shortcuts import render
from .models import Faculty
# Create your views here.

def faculty_list(request):
    faculty = Faculty.objects.all().order_by('name')
    return render(request, 'PeopleApp/FacultyList.html', {'faculty': faculty})
