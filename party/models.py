import datetime
from django.db import models

from system.models import BaseModel
from account.models import Account
from .choices import PartyType, PartyGender


class PartySubType(BaseModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128, blank=True)
    label = models.CharField(max_length=128, blank=True)
    type = models.IntegerField(choices=PartyType.choices, default=PartyType.Customer)

    def __str__(self):
        return self.name

    @property
    def type_text(self):
        return self.get_type_display()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.label:
            self.label = self.name
        # TODO: code should be unique, handle uniqueness using uuid
        self.code = str(self.name).strip().lower().replace(' ', '-')
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class Party(BaseModel):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64, null=True)
    code = models.CharField(max_length=16, null=True, blank=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    entry_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    gender = models.IntegerField(choices=PartyGender.choices, default=PartyGender.Male, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True)
    currency = models.CharField(max_length=64, null=True, blank=True)
    bank_account_name = models.CharField(max_length=64, null=True, blank=True)
    bank_account_number = models.CharField(max_length=64, null=True, blank=True)
    passport = models.CharField(max_length=64, null=True, blank=True)
    etin = models.CharField(max_length=64, null=True, blank=True)
    bin = models.CharField(max_length=64, null=True, blank=True)
    vat_reg_no = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def gender_text(self):
        return self.get_gender_display()


class Customer(Party):
    type = models.IntegerField(choices=PartyType.choices, default=PartyType.Customer)

    def __str__(self):
        return f'{self.name} # {self.type_text}'

    @property
    def type_text(self):
        return self.get_type_display()


class Vendor(Party):
    type = models.IntegerField(choices=PartyType.choices, default=PartyType.Vendor)

    def __str__(self):
        return f'{self.name} # {self.type_text}'

    @property
    def type_text(self):
        return self.get_type_display()
