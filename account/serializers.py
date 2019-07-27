from rest_framework import serializers

from .models import AccountSubType, Account


class AccountSubTypeSerializer(serializers.ModelSerializer):
    """TODO: don't use ModelSerializer, use normal Serializer"""
    class Meta:
        model = AccountSubType
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    """TODO: don't use ModelSerializer, use normal Serializer"""
    class Meta:
        model = Account
        fields = '__all__'
