import random

import pytest
import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice

from ...choices import AccountType
from ...models import AccountSubType
from ...serializers import AccountSubTypeSerializer
from ..factory import AccountSubTypeFactory

fake = Faker()


class TestAccountSubTypeSerializer:

    def test_create(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory,
                             name=name,
                             created_by=user.pk,
                             type=FuzzyChoice(choices=AccountType.values.keys()),
                             order=random.randint(0, 10))

        serializer = AccountSubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = AccountSubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name

    @pytest.mark.django_db
    def test_create_name_error(self):
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory)
        del data['name']

        serializer = AccountSubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_update(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name, created_by=user)
        sub_type = AccountSubTypeFactory()

        serializer = AccountSubTypeSerializer()
        serializer.update(sub_type, data)

        query = AccountSubType.objects.all()
        saved_sub_type = query.first()

        assert query.count() == 1
        assert saved_sub_type.name == name