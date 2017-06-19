from django.shortcuts import render
from .models import Events

def event(request):
    events = Events.objects.all().order_by("date")
    return render(request, 'events.html', {'events': events})
