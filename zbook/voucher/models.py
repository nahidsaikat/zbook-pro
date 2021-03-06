import datetime
from django.db import models

from zbook.system.models import BaseModel
from zbook.account.models import Account
from zbook.party.models import Party
from .choices import VoucherType


class VoucherSubType(BaseModel):
    type = models.IntegerField(choices=VoucherType.choices, default=VoucherType.Receive)
    name = models.CharField(max_length=64)
    prefix = models.CharField(max_length=64)
    no_start_from = models.IntegerField(default=1000, null=True, blank=True)
    debit_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='voucher_sub_type_debit_account')
    credit_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='voucher_sub_type_credit_account')

    def __str__(self):
        return f'{self.name} # {self.type_text}'

    @property
    def type_text(self):
        return self.get_type_display()


class Voucher(BaseModel):
    voucher_number = models.CharField(max_length=64, blank=True)
    voucher_date = models.DateField(default=datetime.date.today)
    type = models.IntegerField(choices=VoucherType.choices, default=VoucherType.Receive, null=True, blank=True)
    sub_type = models.ForeignKey(VoucherSubType, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=15, decimal_places=6)
    party = models.ForeignKey(Party, on_delete=models.DO_NOTHING, null=True, blank=True)
    ref_voucher = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    accounts = models.ManyToManyField(Account, blank=True)
    # TODO: Needs to bring exchange_rate column

    def __str__(self):
        return f'{self.voucher_number} # {self.type_text}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if hasattr(self, 'sub_type'):
            self.type = self.sub_type.type
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    @property
    def type_text(self):
        return self.get_type_display()

    @property
    def sub_type_text(self):
        return self.sub_type.name

    @property
    def party_name(self):
        return self.party.name

    @property
    def ref_voucher_number(self):
        return self.ref_voucher.voucher_number

    @property
    def accounts_name(self):
        return ', '.join([account.name for account in self.accounts.all()])


class Ledger(BaseModel):
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    entry_date = models.DateField(default=datetime.date.today, blank=True)
    amount = models.DecimalField(default=0, max_digits=15, decimal_places=6)
    account_amount = models.DecimalField(default=0, max_digits=15, decimal_places=6, blank=True)
    description = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.voucher.voucher_number} # {self.voucher.voucher_number} # {self.account.name} # {self.amount}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # TODO: Change according to currency app
        self.account_amount = self.amount
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    @property
    def other_accounts(self):
        return self.voucher.accounts.exclude(id=self.account.pk)

    @property
    def other_accounts_name(self):
        return [account.name for account in self.other_accounts]
