from rest_framework import serializers

from .models import PartySubType, Customer


class PartySubTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartySubType
        fields = '__all__'
        read_only_fields = ('code', )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
