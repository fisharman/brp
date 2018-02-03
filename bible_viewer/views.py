from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.html import format_html

from .apps import date_dict
from .models import Chapters


# Create your views here.
def index(request):

    current_date = timezone.localtime(timezone.now()).date()

    if current_date in date_dict and Chapters.objects.filter(reference_osis=date_dict[current_date]):
        content = Chapters.objects.get(reference_osis=date_dict[current_date])#.content
    else:
        content = "Today is Catch-Up/Evaluation Day"

    return render(request, 'bible_viewer/index.html', {'output': content})
    # return HttpResponse(content)