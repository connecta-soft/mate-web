# Generated by Django 4.1 on 2023-02-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_applications_admin_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='distance',
            field=models.CharField(default='some', max_length=255, verbose_name='Distance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leads',
            name='distance',
            field=models.CharField(default='some', max_length=255, verbose_name='Distance'),
            preserve_default=False,
        ),
    ]
