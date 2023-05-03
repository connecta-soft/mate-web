# Generated by Django 4.1 on 2023-02-11 19:22

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_applications_distance_alter_leads_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='car_year',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[main.models.is_numeric_validator], verbose_name='Car year'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='distance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Distance'),
        ),
    ]