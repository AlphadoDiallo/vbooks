# Generated by Django 3.1.1 on 2020-10-08 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.CharField(max_length=100)),
                ('spread', models.CharField(max_length=100)),
                ('underdog', models.CharField(max_length=100)),
                ('list_total', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
                ('list_data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
