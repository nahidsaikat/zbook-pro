import datetime
from django.db import models

from .choices import AccountType


class AccountSubType(models.Model):
    """TODO: inherit from system base model"""
    name = models.CharField(max_length=64)
    type = models.IntegerField(choices=AccountType.choices, default=AccountType.Asset)
    order = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.name}#{self.get_type_display()}#{self.order}'


class Account(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, null=True, blank=True)
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=64)
    type = models.IntegerField(choices=AccountType.choices, default=AccountType.Asset, blank=True)
    sub_type = models.ForeignKey(AccountSubType, on_delete=models.DO_NOTHING)
    depth = models.IntegerField(default=0, null=True, blank=True)
    entry_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
