from django.shortcuts import render
from .models import NoticeBoard, Events, News, Research, QuickLinks

def index(request):
    notice = NoticeBoard.objects.all().order_by("-date")
    events = Events.objects.all().order_by("-date")
    news = News.objects.all().order_by("-date")
    research = Research.objects.all().order_by("-date")
    quicklinks = QuickLinks.objects.all().order_by("-date")
    object_list = {'notice': notice, 'events': events, 'news': news, 'research': research, 'quicklinks': quicklinks}
    return render(request, 'home.html', object_list)
