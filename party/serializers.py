from rest_framework import serializers

from .models import PartySubType, Customer, Vendor


class PartySubTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartySubType
        fields = '__all__'
        read_only_fields = ('code', )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'
