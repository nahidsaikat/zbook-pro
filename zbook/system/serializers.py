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
