# Generated by Django 2.2.4 on 2019-08-15 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger',
            name='party',
        ),
        migrations.AddField(
            model_name='ledger',
            name='account_amount',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=15),
        ),
    ]
