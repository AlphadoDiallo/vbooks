from django.db import models
from datetime import datetime


class College(models.Model):
    favorite = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)
    underdog = models.CharField(max_length=100)
    list_total = models.CharField(max_length=100)
    win = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    list_data = models.CharField(max_length=100)

    def __str__(self):
        return self.favorite
