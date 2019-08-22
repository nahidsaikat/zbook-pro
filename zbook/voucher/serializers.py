from django.db import transaction

from zbook.system.serializers import BaseSerializer
from zbook.account.models import Account
from .models import VoucherSubType, Voucher, Ledger


class VoucherSubTypeSerializer(BaseSerializer):

    class Meta:
        model = VoucherSubType
        fields = '__all__'


class LedgerCreateSerializer(BaseSerializer):

    def to_internal_value(self, data):
        ledgers = data.get('ledgers', [])
        data = super().to_internal_value(data)
        data['ledgers'] = ledgers
        return data

    def create(self, validated_data):
        with transaction.atomic():
            ledger_list = validated_data.pop('ledgers', [])
            instance = super().create(validated_data)
            for ledger in ledger_list:
                account = Account.objects.get(pk=ledger.get('account_id'))
                amount = ledger.get('amount')
                Ledger.objects.create(voucher=instance, account=account, amount=amount, created_by=instance.created_by)
        return instance

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance = super().update(instance, validated_data)
        return instance


class VoucherSerializer(LedgerCreateSerializer):

    class Meta:
        model = Voucher
        fields = '__all__'
