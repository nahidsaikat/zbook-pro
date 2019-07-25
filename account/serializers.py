from rest_framework import serializers

from .models import AccountSubType


class AccountSubTypeSerializer(serializers.ModelSerializer):
    """TODO: don't use ModelSerializer, use normal Serializer"""
    class Meta:
        model = AccountSubType
        fields = '__all__'
