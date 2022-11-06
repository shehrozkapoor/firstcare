# Generated by Django 4.0.3 on 2022-03-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0003_patient_deceasedboolean_patient_deceaseddatetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='privilage_member',
            new_name='privilege_member',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='registeration_date',
            new_name='registration_date',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='registeration_type',
            new_name='registration_type',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='thrid_name_arabic',
            new_name='third_name_arabic',
        ),
        migrations.AlterField(
            model_name='patient',
            name='maritail_status',
            field=models.CharField(blank=True, choices=[('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE')], max_length=10, null=True),
        ),
    ]