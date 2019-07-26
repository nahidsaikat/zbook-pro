import datetime
from django.db import models

from system.models import BaseModel
from account.models import Account
from .choices import PartyType, PartyGender


class Party(BaseModel):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16, null=True)
    email = models.EmailField(max_length=64, null=True)
    code = models.CharField(max_length=16, null=True, blank=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    entry_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    gender = models.IntegerField(choices=PartyGender.choices, default=PartyGender.Male, null=True, blank=True)
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True)
    currency = models.CharField(max_length=64, null=True, blank=True)
    bank_account_name = models.CharField(max_length=64, null=True, blank=True)
    bank_account_number = models.CharField(max_length=64, null=True, blank=True)
    passport = models.CharField(max_length=64, null=True, blank=True)
    etin = models.CharField(max_length=64, null=True, blank=True)
    bin = models.CharField(max_length=64, null=True, blank=True)
    vat_reg_no = models.CharField(max_length=64, null=True, blank=True)


class Customer(Party):
    type = models.IntegerField(choices=PartyType.choices, default=PartyType.Customer)


class Vendor(Party):
    type = models.IntegerField(choices=PartyType.choices, default=PartyType.Vendor)
