# Generated by Django 4.0.3 on 2022-06-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_management', '0002_department_fhir_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fhir_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]