# Generated by Django 4.1 on 2024-03-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_leads2_vehicle_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads2',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
