from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.html import format_html

from .apps import date_dict
from .models import Chapters, Annotations


# Create your views here.
def index(request):

    current_date = timezone.localtime(timezone.now()).date()

    if current_date in date_dict and Chapters.objects.filter(reference_osis=date_dict[current_date]):
        chapters = Chapters.objects.get(reference_osis=date_dict[current_date])
        annotations = Annotations.objects.filter(osis=date_dict[current_date])
    else:
        chapters = "Today is Catch-Up/Evaluation Day"

    # for testing only!
    #chapters = Chapters.objects.get(reference_osis="Matt.7")
    #annotations = Annotations.objects.filter(osis="Matt.7")

    return render(request, 'bible_viewer/index.html', {'chapters': chapters, 'annotations': annotations})
    # return HttpResponse(content)