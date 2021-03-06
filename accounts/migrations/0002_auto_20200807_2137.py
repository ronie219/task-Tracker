# Generated by Django 3.1 on 2020-08-07 16:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='coment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='Status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterUniqueTogether(
            name='tasks',
            unique_together={('user', 'status', 'updated_at')},
        ),
    ]
