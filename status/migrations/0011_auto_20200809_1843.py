# Generated by Django 3.1 on 2020-08-09 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0010_auto_20200809_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='starting_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 9, 18, 43, 47, 491174)),
        ),
    ]
