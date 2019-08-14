from zbook.system.serializers import BaseSerializer
from .models import VoucherSubType


class VoucherSubTypeSerializer(BaseSerializer):

    class Meta:
        model = VoucherSubType
        fields = '__all__'
