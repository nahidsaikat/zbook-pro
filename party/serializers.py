from rest_framework import serializers

from .models import PartySubType


class PartySubTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartySubType
        fields = '__all__'
