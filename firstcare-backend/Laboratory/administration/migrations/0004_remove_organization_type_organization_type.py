# Generated by Django 4.0.3 on 2022-07-13 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_organization_nphies_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='type',
        ),
        migrations.AddField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.organizationtype'),
        ),
    ]