# Generated by Django 3.1 on 2020-08-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0012_auto_20200809_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='starting_date',
            field=models.DateField(blank=True, default='1999-01-01'),
        ),
    ]
