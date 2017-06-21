from django.shortcuts import render
from .models import Projects

def projects(request):
    pro = Projects.objects.all().order_by("title")
    object_list = {'projects': pro}
    return render(request, 'projects.html', object_list)
