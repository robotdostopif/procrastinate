# Generated by Django 4.1.5 on 2023-01-06 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 11, 7, 49, 71699, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]