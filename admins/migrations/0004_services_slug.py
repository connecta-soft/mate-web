# Generated by Django 4.1 on 2023-05-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admins", "0003_remove_eventimages_event_delete_faq_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="slug",
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
