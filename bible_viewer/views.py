import random

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.utils.html import format_html

from .apps import date_dict
from .models import Chapters, Annotations


# Create your views here.
def index(request, version='NLT2013'):
    current_date = timezone.localtime(timezone.now()).date()

    chapters, annotations = content_lookup(current_date)
    return render(request, 'bible_viewer/index.html', {'chapters': chapters,
                                                       'annotations': annotations,
                                                       'current_date': current_date.strftime('%d-%m-%Y')})
    # return HttpResponse(content)


def set_date(request, version, date):
    if date is None:
        #raise Http404("Invalid Date")
        # Todo 3: Invalid date should fail gracefully
        chapters, annotations = None, None
    else:
        chapters, annotations = content_lookup(date)

    return render(request, 'bible_viewer/index.html', {'chapters': chapters,
                                                       'annotations': annotations,
                                                       'current_date': date.strftime('%d-%m-%Y')})


def content_lookup(current_date):
    if current_date in date_dict and Chapters.objects.filter(reference_osis=date_dict[current_date]):
        # Todo 4: change to get_object_or_404
        chapters = Chapters.objects.get(reference_osis=date_dict[current_date])
        annotations = Annotations.objects.filter(osis=date_dict[current_date])
    else:
        # change to select random chapter and display alert
        # pick random between 1 and 1189
        # Todo 5: off days will generate a JS alert and show random chapter
        chapters = None
        annotations = None

    return chapters, annotations