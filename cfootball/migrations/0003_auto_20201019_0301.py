# Generated by Django 3.1.2 on 2020-10-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfootball', '0002_college_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='list_data',
            field=models.CharField(max_length=100),
        ),
    ]
