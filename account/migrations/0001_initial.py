# Generated by Django 2.2.1 on 2019-05-14 00:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.IntegerField(choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Income'), (4, 'Expense'), (5, 'Equity')], default=1)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=64)),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Income'), (4, 'Expense'), (5, 'Equity')], default=1)),
                ('depth', models.IntegerField(blank=True, default=0, null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
                ('sub_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.AccountSubType')),
            ],
        ),
    ]
