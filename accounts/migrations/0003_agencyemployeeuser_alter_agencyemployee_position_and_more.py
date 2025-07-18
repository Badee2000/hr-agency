# Generated by Django 5.2.1 on 2025-06-08 19:32

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_address_customuser_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyEmployeeUser',
            fields=[
            ],
            options={
                'verbose_name': 'Agency Employee',
                'verbose_name_plural': 'Agency Employees',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='agencyemployee',
            name='position',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('agency_employee', 'Agency Employee'), ('candidate', 'Candidate'), ('company_employee', 'Company Employee')], default='agency_employee', max_length=50),
        ),
    ]
