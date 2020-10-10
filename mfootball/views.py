from django.shortcuts import render
from .models import Monday


def home(request):
    mondays = Monday.objects.all()
    return render(request, 'mfootball/mfootballs.html', {'mondays': mondays})
