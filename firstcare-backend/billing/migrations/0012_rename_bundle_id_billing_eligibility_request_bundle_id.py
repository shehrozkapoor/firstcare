# Generated by Django 4.0.3 on 2022-06-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_billing_bundle_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='bundle_id',
            new_name='eligibility_request_bundle_id',
        ),
    ]