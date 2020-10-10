# Generated by Django 3.1.1 on 2020-09-30 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegasbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.CharField(max_length=100)),
                ('spread', models.CharField(max_length=100)),
                ('underdog', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
                ('list_data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
