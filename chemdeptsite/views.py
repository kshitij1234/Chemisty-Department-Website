from django.shortcuts import render
from .models import NoticeBoard, News, QuickLinks
from research.models import ResearchAreas
from Events.models import Events


def index(request):
    notice = NoticeBoard.objects.all().order_by("-date")
    news = News.objects.all().order_by("-date")
    research = ResearchAreas.objects.all().order_by("title")
    quicklinks = QuickLinks.objects.all().order_by("date")
    events = Events.objects.all().order_by("date")
    object_list = {'notice': notice, 'news': news, 'research': research, 'quicklinks': quicklinks, 'events': events}
    return render(request, 'home.html', object_list)

def facilities(request):
    return render(request, 'facilities.html')

def error_404(request):
    return render(request, 'error_404.html')
