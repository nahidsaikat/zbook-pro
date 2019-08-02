from system.serializers import BaseSerializer
from .models import AccountSubType, Account


class AccountSubTypeSerializer(BaseSerializer):
    """TODO: don't use ModelSerializer, use normal Serializer"""
    class Meta:
        model = AccountSubType
        fields = '__all__'


class AccountSerializer(BaseSerializer):
    """TODO: don't use ModelSerializer, use normal Serializer"""
    class Meta:
        model = Account
        fields = '__all__'
