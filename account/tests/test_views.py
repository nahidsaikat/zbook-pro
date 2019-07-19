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
