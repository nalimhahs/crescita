from django.shortcuts import render
from django.http import Http404

from .models import Event, Catagory

# Create your views here.


def homePage(request):
    catagories = Catagory.objects.all()
    return render(request, 'index.html', {'catagories': catagories})


def aboutPage(request):
    return render(request, 'about.html', {})


def contactPage(request):
    return render(request, 'contact.html', {})


def catagoryListing(request, catagory):
    events = Event.objects.filter(catagory__slug=catagory)
    try:
        p = Catagory.objects.get(name=catagory)
    except Catagory.DoesNotExist:
        raise Http404
    return render(request, 'events/eventlist.html', {'events': events, 'catagory': p})


def eventListing(request, catagory, event_slug):
    event = Event.objects.filter(event_slug=event_slug)
    try:
        e = event[0]
    except IndexError as err:
        raise Http404
    return render(request, 'events/singleevent.html', {'event': e, 'eventName': e.name})
