# Generated by Django 4.1 on 2024-02-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_applications_business_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_year', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('nbm', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_via_id', models.IntegerField(choices=[(1, '1'), (2, '2')], max_length=255, verbose_name='Ship via id')),
                ('vehicle', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_runs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, verbose_name='Vehicle Runs')),
                ('ship_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship2_fromappl', to='main.city')),
                ('ship_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship2_to_appl', to='main.city')),
            ],
        ),
    ]
