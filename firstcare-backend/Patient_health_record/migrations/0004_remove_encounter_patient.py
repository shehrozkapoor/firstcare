# Generated by Django 4.0.3 on 2022-06-11 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient_health_record', '0003_remove_encounter_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='patient',
        ),
    ]
