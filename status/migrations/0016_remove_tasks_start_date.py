# Generated by Django 3.1 on 2020-08-09 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0015_auto_20200809_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='start_date',
        ),
    ]
