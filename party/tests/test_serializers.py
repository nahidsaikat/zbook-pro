import factory
from faker import Faker

from ..serializers import PartySubTypeSerializer
from ..models import PartySubType
from .factory import PartySubTypeFactory

fake = Faker()


class TestPartySubTypeSerializer:

    def test_create(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory,
                             name=name,
                             created_by=user.pk)

        serializer = PartySubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = PartySubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name

    def test_create_name_error(self):
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory)
        del data['name']

        serializer = PartySubTypeSerializer(data=data)
        assert not serializer.is_valid()
