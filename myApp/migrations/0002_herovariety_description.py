# Generated by Django 5.0.6 on 2024-06-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="herovariety",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
