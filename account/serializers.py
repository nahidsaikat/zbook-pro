from rest_framework import serializers

from account.models import AccountSubType


class AccountSubTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountSubType
        fields = '__all__'
