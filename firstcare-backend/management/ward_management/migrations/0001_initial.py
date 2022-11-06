# Generated by Django 4.0.2 on 2022-02-11 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bed_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('layout', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='bed_management.bedlayout')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hospital', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='ward_management.hospital')),
                ('room', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='ward_management.room')),
            ],
        ),
    ]