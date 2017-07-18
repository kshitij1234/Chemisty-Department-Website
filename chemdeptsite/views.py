from django.shortcuts import render
from .models import NoticeBoard, News, QuickLinks, HeadsDesk
from research.models import ResearchAreas
from Events.models import Events
from PeopleApp.models import Faculty


def individual_news(request, pk=1):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return render(request, 'error_404.html')
    return render(request, 'individual_news.html', {'news': news})


def index(request):
    notice = NoticeBoard.objects.all().order_by("-date")
    new_article = News.objects.order_by("-date")[:5]
    research = ResearchAreas.objects.all().order_by("title")
    quicklinks = QuickLinks.objects.all().order_by("date")
    events = Events.objects.all().order_by("date")
    object_list = {'notice': notice, 'news': new_article, 'research': research, 'quicklinks': quicklinks,
                   'events': events}
    return render(request, 'home.html', object_list)


def facilities(request):
    return render(request, 'facilities.html')


def error_404(request):
    return render(request, 'error_404.html')


def sitemap(request):
    new_article = News.objects.order_by("-date")
    faculty = Faculty.objects.all().order_by("list_position")
    object_list = {'news': new_article, 'faculty': faculty}
    return render(request, 'sitemap.html', object_list)


def head_msg(request):
    headsdesk = HeadsDesk.objects.all().order_by("-id")
    return render(request, 'head_msg.html', {'headsdesk': headsdesk})


def head_profile(request):
    headsdesk = HeadsDesk.objects.all().order_by("-id")
    return render(request, 'head_profile.html', {'headsdesk': headsdesk})


def news(request):
    news_articles = News.objects.all().order_by("-date")
    return render(request, 'news.html', {
        'news': news_articles
    })


def admissions_postgraduate(request):
    return render(request, 'postgraduate_admissions.html')


def admissions_doctoral(request):
    return render(request, 'doctoral_admissions.html')
