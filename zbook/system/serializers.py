from django.db import transaction
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):

    @property
    def request(self):
        return self.context.get('request')

    def to_internal_value(self, data):
        if self.request and self.request.user:
            data['created_by'] = self.request.user.pk
        ret = super().to_internal_value(data)
        return ret


class LedgerCreateSerializerMixin:

    def create(self, validated_data):

        with transaction.atomic():
            instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):

        with transaction.atomic():
            instance = super().update(instance, validated_data)
        return instance
