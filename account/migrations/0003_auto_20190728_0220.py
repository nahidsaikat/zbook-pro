# Generated by Django 2.2.3 on 2019-07-28 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190726_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='number',
            new_name='code',
        ),
    ]
