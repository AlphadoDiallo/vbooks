# Generated by Django 3.1.2 on 2020-10-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfootball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunday',
            name='win',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
