# Generated by Django 4.0.2 on 2022-02-11 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContributionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deductable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.CharField(blank=True, max_length=100, null=True)),
                ('in_patient', models.CharField(blank=True, max_length=100, null=True)),
                ('out_patient', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_num', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('poverty_status', models.BooleanField(default=False)),
                ('confirmation_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.confirmationtype')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FirstServicePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HeadInsuree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_num', models.CharField(blank=True, max_length=100, null=True)),
                ('given_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'RATHER NOT TO SAY')], max_length=1, null=True)),
                ('maritial_status', models.CharField(choices=[('1', 'MARRIED'), ('2', 'SINGLE')], max_length=1, null=True)),
                ('beneficiary_card', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('id_num', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('photo_date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('1', 'HEAD-INSURANCE'), ('2', 'INSURANCE')], max_length=1, null=True)),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.education')),
            ],
        ),
        migrations.CreateModel(
            name='HealthFacilityLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceUserPermision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LegalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remunerated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.CharField(blank=True, max_length=100, null=True)),
                ('in_patient', models.CharField(blank=True, max_length=100, null=True)),
                ('out_patient', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyHolders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('trade_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('fax', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('accountancy_account', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_date', models.DateField(null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('activity_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.activitycode')),
                ('leagal_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.legalform')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(null=True)),
                ('effective_date', models.DateField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.insuranceuser')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.products')),
            ],
        ),
        migrations.CreateModel(
            name='PoliciesValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('contribution_paid', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.CharField(blank=True, max_length=100, null=True)),
                ('deductable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.deductable')),
                ('remunerated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.remunerated')),
            ],
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.family')),
                ('policy_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.policydetails')),
                ('policy_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.policiesvalues')),
            ],
        ),
        migrations.CreateModel(
            name='Insuree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.family')),
                ('first_service_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.firstservicepoint')),
                ('head_insurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.headinsuree')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceUserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('blocked', models.BooleanField(default=False)),
                ('permisions', models.ManyToManyField(related_name='insurance_user_permissions', to='Insurance.InsuranceUserPermision')),
            ],
        ),
        migrations.AddField(
            model_name='insuranceuser',
            name='role',
            field=models.ManyToManyField(related_name='insurance_user_roles', to='Insurance.InsuranceUserRoles'),
        ),
        migrations.AddField(
            model_name='insuranceuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.family')),
                ('first_service_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.firstservicepoint')),
                ('head_insurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.headinsuree')),
            ],
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.healthfacilitylevel')),
            ],
        ),
        migrations.AddField(
            model_name='headinsuree',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.idtype'),
        ),
        migrations.AddField(
            model_name='headinsuree',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.profession'),
        ),
        migrations.AddField(
            model_name='headinsuree',
            name='relationship_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.relationship'),
        ),
        migrations.AddField(
            model_name='firstservicepoint',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.healthfacility'),
        ),
        migrations.AddField(
            model_name='family',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.familytype'),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('reciept_num', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.contributioncategory')),
                ('payer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.insuranceuser')),
                ('payment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.paymenttype')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.policies')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('policy_holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Insurance.policyholders')),
            ],
        ),
    ]
