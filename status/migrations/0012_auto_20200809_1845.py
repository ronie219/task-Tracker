# Generated by Django 3.1 on 2020-08-09 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0011_auto_20200809_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='starting_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
