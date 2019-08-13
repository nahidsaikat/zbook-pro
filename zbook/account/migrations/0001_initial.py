# Generated by Django 2.2.4 on 2019-08-12 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Income'), (4, 'Expense'), (5, 'Equity')], default=1)),
                ('depth', models.IntegerField(blank=True, default=0, null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(max_length=64)),
                ('type', models.IntegerField(choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Income'), (4, 'Expense'), (5, 'Equity')], default=1)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]