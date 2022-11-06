# Generated by Django 4.0.2 on 2022-02-11 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HCFA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onset_date', models.DateField(blank=True, null=True)),
                ('initial_visit_date', models.DateField(blank=True, null=True)),
                ('prepopulate_last_related_visit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePlanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(blank=True, choices=[('Spouse', 'Spouse'), ('Grandparent', 'Grandparent'), ('Grandchild', 'Grandchild'), ('Nephew or Niece', 'Nephew or Niece'), ('Foster Child', 'Foster Child'), ('Ward', 'Ward'), ('Stepson or Stepdaughter', 'Stepson or Stepdaughter'), ('Child', 'Child'), ('Employee', 'Employee'), ('Unknown', 'Unknown'), ('Handicapped Dependent', 'Handicapped Dependent'), ('Sponsored Dependent', 'Sponsored Dependent'), ('Dependent of a Minor Dependent', 'Dependent of a Minor Dependent'), ('Significant Other', 'Significant Other'), ('Mother', 'Mother'), ('Father', 'Father'), ('Emancipated Minor', 'Emancipated Minor'), ('Organ Donor', 'Organ Donor'), ('Cadaver Donor', 'Cadaver Donor'), ('Injured Plaintiff', 'Injured Plaintiff'), ('Child Where Insured Has No Financial Responsibility', 'Child Where Insured Has No Financial Responsibility'), ('Life Partner', 'Life Partner'), ('Dependent', 'Dependent'), ('Other Relationship', 'Other Relationship')], max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER'), ('UNKNOWN', 'UNKNOWN'), ('DECLINE TO SPECIFY', 'DECLINE TO SPECIFY')], max_length=20, null=True)),
                ('suffix', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('ssn', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tpl_code', models.CharField(blank=True, max_length=100, null=True)),
                ('id_num', models.CharField(blank=True, max_length=100, null=True)),
                ('group_name', models.CharField(blank=True, max_length=100, null=True)),
                ('group_num', models.CharField(blank=True, max_length=100, null=True)),
                ('plan_name', models.CharField(blank=True, max_length=100, null=True)),
                ('claim_office_num', models.CharField(blank=True, max_length=100, null=True)),
                ('allowed_visits_num', models.CharField(blank=True, max_length=100, null=True)),
                ('card_issue_date', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_front', models.FileField(null=True, upload_to='')),
                ('photo_back', models.FileField(null=True, upload_to='')),
                ('same_person', models.BooleanField(default=True)),
                ('insurance_type', models.CharField(blank=True, choices=[('PRIMARY INSURANCE', 'PRIMARY INSURANCE'), ('SECONDARY INSURANCE', 'SECONDARY INSURANCE'), ('TERTIARY INSURANCE', 'TERTIARY INSURANCE'), ('AUTO ACCIDENT INSURANCE', 'AUTO ACCIDENT INSURANCE'), ('WORKER COMP INSURANCE', 'WORKER COMP INSURANCE'), ('DURABLE MED EQPT INSURANCE', 'DURABLE MED EQPT INSURANCE')], max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drchrono_insurance.insurancecompany')),
                ('hcfa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drchrono_insurance.hcfa')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
                ('plan_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drchrono_insurance.insuranceplantype')),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drchrono_insurance.subscriber')),
            ],
        ),
    ]