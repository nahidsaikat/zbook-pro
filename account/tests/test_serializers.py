import random

import pytest
import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice

from account.choices import AccountType
from account.models import AccountSubType
from account.serializers import AccountSubTypeSerializer
from account.tests.factory import AccountSubTypeFactory

fake = Faker()


class TestAccountSubTypeSerializer:

    @pytest.mark.django_db
    def test_create(self):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory,
                             name=name,
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
    def test_update(self):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name)
        sub_type = AccountSubTypeFactory()

        serializer = AccountSubTypeSerializer()
        serializer.update(sub_type, data)

        query = AccountSubType.objects.all()
        saved_sub_type = query.first()

        assert query.count() == 1
        assert saved_sub_type.name == name
