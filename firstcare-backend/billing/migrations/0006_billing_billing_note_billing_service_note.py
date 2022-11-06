# Generated by Django 4.0.2 on 2022-02-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_billing_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='billing_note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='service_note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]