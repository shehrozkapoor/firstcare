# Generated by Django 4.0.3 on 2022-03-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headinsuree',
            name='maritial_status',
            field=models.CharField(choices=[('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE')], max_length=10, null=True),
        ),
    ]
