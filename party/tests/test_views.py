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

    def test_create_name_error(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, created_by=user.pk)

        del data['name']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_unauthorize(self, client, user):
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, created_by=user.pk, name=fake.name())

        response = client.post(self.url, data)

        assert response.status_code == 401

    def test_get_list(self, auth_client, user):
        PartySubTypeFactory(created_by=user)
        PartySubTypeFactory(created_by=user)
        PartySubTypeFactory(created_by=user)

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, user):
        PartySubTypeFactory(created_by=user)
        PartySubTypeFactory(created_by=user)
        PartySubTypeFactory(created_by=user)

        response = client.get(self.url)

        assert response.status_code == 401


class TestPartySubTypeRetrieveUpdateAPIView:

    def test_update_name(self, auth_client, user):
        subtype = PartySubTypeFactory(created_by=user)
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, name=name, created_by=user.pk)

        url = reverse('party:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('name') == name
        assert response.data.get('code') == name.strip().lower().replace(' ', '-')

    def test_update_label(self, auth_client, user):
        subtype = PartySubTypeFactory(created_by=user)
        label = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, label=label, created_by=user.pk)

        url = reverse('party:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('label') == label
