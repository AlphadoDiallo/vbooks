from django.shortcuts import render
from .models import Sunday


def home(request):
    sundays = Sunday.objects.all()
    return render(request, 'sfootball/sfootballs.html', {'sundays': sundays})
