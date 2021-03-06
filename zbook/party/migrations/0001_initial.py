# Generated by Django 2.2.4 on 2019-08-12 13:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=64, null=True)),
                ('code', models.CharField(blank=True, max_length=16, null=True)),
                ('company_name', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], default=1, null=True)),
                ('currency', models.CharField(blank=True, max_length=64, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=64, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=64, null=True)),
                ('passport', models.CharField(blank=True, max_length=64, null=True)),
                ('etin', models.CharField(blank=True, max_length=64, null=True)),
                ('bin', models.CharField(blank=True, max_length=64, null=True)),
                ('vat_reg_no', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartySubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(blank=True, max_length=128)),
                ('label', models.CharField(blank=True, max_length=128)),
                ('type', models.IntegerField(choices=[(1, 'Customer'), (2, 'Vendor')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='party.Party')),
                ('type', models.IntegerField(choices=[(1, 'Customer'), (2, 'Vendor')], default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('party.party',),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('party_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='party.Party')),
                ('type', models.IntegerField(choices=[(1, 'Customer'), (2, 'Vendor')], default=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('party.party',),
        ),
    ]
