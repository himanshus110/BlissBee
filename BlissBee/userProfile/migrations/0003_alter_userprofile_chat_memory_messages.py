# Generated by Django 4.2.5 on 2023-09-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "userProfile",
            "0002_userprofile_chat_memory_messages_userprofile_gender_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="chat_memory_messages",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]