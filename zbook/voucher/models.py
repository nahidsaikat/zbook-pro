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


class Voucher(BaseModel):
    voucher_number = models.CharField(max_length=64, blank=True)
    voucher_date = models.DateField(default=datetime.date.today)
    type = models.IntegerField(choices=VoucherType.choices, default=VoucherType.Receive, null=True, blank=True)
    sub_type = models.ForeignKey(VoucherSubType, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(default=0, max_digits=15, decimal_places=6)
    party = models.ForeignKey(Party, on_delete=models.DO_NOTHING, null=True, blank=True)
    ref_voucher = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    accounts = models.ManyToManyField(Account, blank=True)


class Ledger(BaseModel):
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    party = models.ForeignKey(Party, on_delete=models.DO_NOTHING, null=True, blank=True)
    entry_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=15, decimal_places=6)
    description = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.voucher.voucher_number} - {self.voucher.voucher_date} - {self.account.name} - {self.amount}"

    @property
    def other_accounts(self):
        return self.voucher.accounts.exclude(account_id=self.account_id)

    @property
    def other_accounts_name(self):
        return [account.name for account in self.other_accounts]
