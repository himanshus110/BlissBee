# Generated by Django 4.2.5 on 2023-09-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userProfile", "0006_scenariofeedback_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="scenariofeedback",
            name="title",
            field=models.TextField(default=""),
        ),
    ]