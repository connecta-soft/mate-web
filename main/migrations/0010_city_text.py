# Generated by Django 4.1 on 2023-02-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_leads_email_leads_nbm_leads_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='text',
            field=models.JSONField(blank=True, null=True, verbose_name='Text'),
        ),
    ]