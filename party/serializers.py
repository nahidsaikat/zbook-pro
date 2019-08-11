from system.serializers import BaseSerializer
from .models import PartySubType, Customer, Vendor


class PartySubTypeSerializer(BaseSerializer):

    class Meta:
        model = PartySubType
        fields = '__all__'
        read_only_fields = ('code', )


class CustomerSerializer(BaseSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class VendorSerializer(BaseSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'
