from django.db import models

from account.models import Account
from .choices import VoucherType


class VoucherSubType(models.Model):
    type = models.IntegerField(choices=VoucherType.choices, default=VoucherType.Receive)
    name = models.CharField(max_length=64)
    prefix = models.CharField(max_length=64)
    no_start_from = models.IntegerField(default=1000, null=True, blank=True)
    debit_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='voucher_sub_type_debit_account')
    credit_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='voucher_sub_type_credit_account')
