from django.urls import path
from . import views
# mfootball
urlpatterns = [
    path('', views.home, name='mfootballs'),

]
