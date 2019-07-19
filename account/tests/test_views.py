import factory, random
from faker import Faker
from factory.fuzzy import FuzzyChoice

from django.urls import reverse
from django.contrib.auth import get_user_model

from .factory import AccountSubTypeFactory
from ..choices import AccountType

User = get_user_model()
fake = Faker()


class TestAccountSubTypeListCreateAPIView:

    url = reverse('account:subtype:list-create')

    def test_create(self, auth_client):
        name = fake.name()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        order = random.randint(0, 10)
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name, type=_type, order=order)

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('name') == name
        assert response.data.get('type') == _type
        assert response.data.get('order') == order

    def test_create_name(self, auth_client):
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory)
        del data['name']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_unauthorize(self, client):
        name = fake.name()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        order = random.randint(0, 10)
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name, type=_type, order=order)

        response = client.post(self.url, data)

        assert response.status_code == 401

    def test_get_list(self, auth_client):
        AccountSubTypeFactory()
        AccountSubTypeFactory()
        AccountSubTypeFactory()

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, db):
        AccountSubTypeFactory()
        AccountSubTypeFactory()
        AccountSubTypeFactory()

        response = client.get(self.url)

        assert response.status_code == 401


class TestAccountSubTypeRetrieveUpdateAPIView:

    def test_update_name(self, auth_client):
        subtype = AccountSubTypeFactory()
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('name') == name

    def test_update_type(self, auth_client):
        subtype = AccountSubTypeFactory()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, type=_type)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('type') == _type

    def test_update_order(self, auth_client):
        subtype = AccountSubTypeFactory()
        order = random.randint(0, 10)
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, order=order)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('order') == order

    def test_update_unauthorize(self, client, db):
        subtype = AccountSubTypeFactory()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = client.patch(url, data)

        assert response.status_code == 401

    def test_get_subtype(self, auth_client):
        subtype = AccountSubTypeFactory()
        url = reverse('account:subtype:detail-update', args=[subtype.pk])

        response = auth_client.get(url)

        assert response.status_code == 200
        assert response.data.get('name') == subtype.name
        assert response.data.get('type') == subtype.type
        assert response.data.get('order') == subtype.order

    def test_get_subtype_unauthorize(self, client, db):
        subtype = AccountSubTypeFactory()
        url = reverse('account:subtype:detail-update', args=[subtype.pk])

        response = client.get(url)

        assert response.status_code == 401
