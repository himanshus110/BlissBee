# Generated by Django 4.2.5 on 2023-09-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userProfile", "0004_alter_userprofile_moving_summary_buffer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="chat_memory_messages",
            field=models.TextField(blank=True, default="[]", null=True),
        ),
    ]
