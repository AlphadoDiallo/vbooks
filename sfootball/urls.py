from django.urls import path
from . import views
# listings
urlpatterns = [
    path('', views.home, name='sfootballs'),

]
