from django.shortcuts import render
from .models import NoticeBoard, News, QuickLinks
from research.models import ResearchAreas
from Events.models import Events

def index(request):
    notice = NoticeBoard.objects.all().order_by("-date")
    new_article = News.objects.order_by("-date")[:5]
    research = ResearchAreas.objects.all().order_by("title")
    quicklinks = QuickLinks.objects.all().order_by("date")
    events = Events.objects.all().order_by("date")
    object_list = {'notice': notice, 'news': new_article, 'research': research, 'quicklinks': quicklinks, 'events': events}
    return render(request, 'home.html', object_list)


def facilities(request):
    return render(request, 'facilities.html')


def error_404(request):
    return render(request, 'error_404.html')


def sitemap(request):
    return render(request, 'sitemap.html')


def head_msg(request):
    return render(request, 'head_msg.html')


def news(request):
    news_articles = News.objects.all().order_by("-date")
    return render(request, 'news.html', {
        'news': news_articles
    })
