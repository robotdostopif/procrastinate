# Generated by Django 4.1.5 on 2023-01-07 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 7, 19, 19, 27, 947495, tzinfo=datetime.timezone.utc)),
        ),
    ]
