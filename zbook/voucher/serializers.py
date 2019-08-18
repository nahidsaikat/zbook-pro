from zbook.system.serializers import BaseSerializer
from .models import VoucherSubType, Voucher


class VoucherSubTypeSerializer(BaseSerializer):

    class Meta:
        model = VoucherSubType
        fields = '__all__'


class VoucherSerializer(BaseSerializer):

    class Meta:
        model = Voucher
        fields = '__all__'
