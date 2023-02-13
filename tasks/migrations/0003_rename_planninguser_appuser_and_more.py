# Generated by Django 4.1.5 on 2023-02-07 19:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0002_alter_task_created"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PlanningUser",
            new_name="AppUser",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="planning_user",
            new_name="app_user",
        ),
        migrations.AddField(
            model_name="category",
            name="app_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.appuser",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="created",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2023, 2, 7, 19, 21, 21, 98944, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]