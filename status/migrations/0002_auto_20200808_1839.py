# Generated by Django 3.1 on 2020-08-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='detail',
            field=models.CharField(max_length=250),
        ),
    ]
