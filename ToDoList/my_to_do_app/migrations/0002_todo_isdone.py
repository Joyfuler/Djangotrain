# Generated by Django 5.0.6 on 2024-07-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_to_do_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="isDone",
            field=models.BooleanField(default=False),
        ),
    ]
