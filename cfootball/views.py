from django.shortcuts import render
from .models import College


def home(request):
    colleges = College.objects.all()
    return render(request, 'cfootball/cfootballs.html', {'colleges': colleges})
