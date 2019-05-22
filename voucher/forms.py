from django.forms import ModelForm
from .models import VoucherSubType, Voucher, Ledger


class VoucherSubTypeForm(ModelForm):
    class Meta:
        model = VoucherSubType
        fields = '__all__'


class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = '__all__'


class LedgerForm(ModelForm):
    class Meta:
        model = Ledger
        fields = '__all__'
