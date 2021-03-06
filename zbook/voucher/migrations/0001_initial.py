# Generated by Django 2.2.4 on 2019-08-12 13:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('party', '0001_initial'),
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Receive'), (2, 'Payment'), (3, 'Expense'), (4, 'Sale'), (5, 'Purchase'), (6, 'SaleDelivery'), (7, 'PurchaseDelivery')], default=1)),
                ('name', models.CharField(max_length=64)),
                ('prefix', models.CharField(max_length=64)),
                ('no_start_from', models.IntegerField(blank=True, default=1000, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vouchersubtype_created_by', to=settings.AUTH_USER_MODEL)),
                ('credit_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucher_sub_type_credit_account', to='account.Account')),
                ('debit_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucher_sub_type_debit_account', to='account.Account')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vouchersubtype_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('voucher_number', models.CharField(blank=True, max_length=64)),
                ('voucher_date', models.DateField(default=datetime.date.today)),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Receive'), (2, 'Payment'), (3, 'Expense'), (4, 'Sale'), (5, 'Purchase'), (6, 'SaleDelivery'), (7, 'PurchaseDelivery')], default=1, null=True)),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=15)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('accounts', models.ManyToManyField(blank=True, to='account.Account')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucher_created_by', to=settings.AUTH_USER_MODEL)),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='party.Party')),
                ('ref_voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='voucher.Voucher')),
                ('sub_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voucher.VoucherSubType')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucher_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inactive', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=15)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Account')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ledger_created_by', to=settings.AUTH_USER_MODEL)),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='party.Party')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ledger_updated_by', to=settings.AUTH_USER_MODEL)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voucher.Voucher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
