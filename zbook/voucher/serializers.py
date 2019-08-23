from django.db import transaction

from zbook.system.serializers import BaseSerializer
from zbook.account.models import Account
from .models import VoucherSubType, Voucher, Ledger


class VoucherSubTypeSerializer(BaseSerializer):

    class Meta:
        model = VoucherSubType
        fields = '__all__'


class LedgerCreateSerializer(BaseSerializer):
    # TODO: Add here a ledgers custom field and remove code in to_internal_value method

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
                Ledger.objects.create(voucher=instance, account=account, amount=amount, created_by=instance.created_by,
                                      description=ledger.get('description', ''))
        return instance

    def update(self, instance, validated_data):
        with transaction.atomic():
            ledger_list = validated_data.pop('ledgers', [])
            instance = super().update(instance, validated_data)
            for ledger in ledger_list:
                account = Account.objects.get(pk=ledger.get('account_id'))
                amount = ledger.get('amount')
                defaults = {
                    'voucher': instance,
                    'account': account,
                    'amount': amount,
                    'created_by': instance.created_by,
                    'description': ledger.get('description', '')
                }
                Ledger.objects.update_or_create(id=ledger.get('id'), defaults=defaults)
        return instance


class VoucherSerializer(LedgerCreateSerializer):

    class Meta:
        model = Voucher
        fields = '__all__'
