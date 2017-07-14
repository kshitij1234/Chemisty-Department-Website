from django.shortcuts import render
from .models import Projects, ResearchAreas


def projects(request):
    pro = Projects.objects.all().order_by("title")
    object_list = {'projects': pro}
    return render(request, 'projects.html', object_list)


def areas(request):
    area = ResearchAreas.objects.all().order_by("title")
    object_list = {'areas': area}
    return render(request, 'areas.html', object_list)

def publications(request):
    return render(request, 'error_404.html')
