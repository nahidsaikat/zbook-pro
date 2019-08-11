import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice

from django.urls import reverse
from ..choices import PartyType
from .factory import PartySubTypeFactory

fake = Faker()


class TestPartySubTypeListCreateAPIView:
    url = reverse('party:subtype:list-create')

    def test_create(self, auth_client, user):
        name = fake.name()
        _type = FuzzyChoice(choices=PartyType.values.keys()).fuzz()
        label = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, name=name, type=_type, label=label)

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('name') == name
        assert response.data.get('code') == name.strip().lower().replace(' ', '-')
        assert response.data.get('label') == label
        assert response.data.get('type') == _type
        assert response.data.get('created_by') == user.pk
