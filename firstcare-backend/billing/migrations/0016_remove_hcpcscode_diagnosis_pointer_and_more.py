# Generated by Django 4.0.3 on 2022-06-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0015_alter_hcpcscode_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hcpcscode',
            name='diagnosis_pointer',
        ),
        migrations.RemoveField(
            model_name='hcpcscode',
            name='price',
        ),
        migrations.AddField(
            model_name='hcpcs',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
