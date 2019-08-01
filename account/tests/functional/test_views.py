import factory, random
from faker import Faker
from factory.fuzzy import FuzzyChoice

from django.urls import reverse
from django.contrib.auth import get_user_model

from ..factory import AccountSubTypeFactory, AccountFactory
from ...choices import AccountType

User = get_user_model()
fake = Faker()


class TestAccountSubTypeListCreateAPIView:

    url = reverse('account:subtype:list-create')

    def test_create(self, auth_client, user):
        name = fake.name()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        order = random.randint(0, 10)
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name, type=_type,
                             order=order, created_by=user.pk)

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('name') == name
        assert response.data.get('type') == _type
        assert response.data.get('order') == order

    def test_create_name(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, created_by=user.pk)

        del data['name']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_unauthorize(self, client, user):
        name = fake.name()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        order = random.randint(0, 10)

        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, created_by=user.pk,
                             name=name, type=_type, order=order)

        response = client.post(self.url, data)

        assert response.status_code == 401

    def test_get_list(self, auth_client, user):
        AccountSubTypeFactory(created_by=user)
        AccountSubTypeFactory(created_by=user)
        AccountSubTypeFactory(created_by=user)

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, user):
        AccountSubTypeFactory(created_by=user)
        AccountSubTypeFactory(created_by=user)
        AccountSubTypeFactory(created_by=user)

        response = client.get(self.url)

        assert response.status_code == 401


class TestAccountSubTypeRetrieveUpdateAPIView:

    def test_update_name(self, auth_client, user):
        subtype = AccountSubTypeFactory()
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, name=name, created_by=user.pk)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('name') == name

    def test_update_type(self, auth_client, user):
        subtype = AccountSubTypeFactory()
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, type=_type, created_by=user.pk)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('type') == _type

    def test_update_order(self, auth_client, user):
        subtype = AccountSubTypeFactory()
        order = random.randint(0, 10)
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, order=order, created_by=user.pk)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('order') == order

    def test_update_unauthorize(self, client, user):
        subtype = AccountSubTypeFactory()
        data = factory.build(dict, FACTORY_CLASS=AccountSubTypeFactory, created_by=user.pk)

        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        response = client.patch(url, data)

        assert response.status_code == 401

    def test_get_subtype(self, auth_client, user):
        subtype = AccountSubTypeFactory(created_by=user)
        url = reverse('account:subtype:detail-update', args=[subtype.pk])

        response = auth_client.get(url)

        assert response.status_code == 200
        assert response.data.get('name') == subtype.name
        assert response.data.get('type') == subtype.type
        assert response.data.get('order') == subtype.order

    def test_get_subtype_unauthorize(self, client, user):
        subtype = AccountSubTypeFactory(created_by=user)
        url = reverse('account:subtype:detail-update', args=[subtype.pk])

        response = client.get(url)

        assert response.status_code == 401


class TestAccountListCreateAPIView:

    url = reverse('account:list-create')

    def test_create(self, auth_client, user, sub_type):
        name = fake.name()
        code = fake.random_int(1, 100)
        _type = FuzzyChoice(choices=AccountType.values.keys()).fuzz()
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, name=name, type=_type, code=code,
                             sub_type=sub_type.pk, created_by=user.pk)

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('name') == name
        assert response.data.get('type') == _type
        assert response.data.get('code') == str(code)
        assert response.data.get('sub_type') == sub_type.pk

    def test_create_name(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, created_by=user.pk)
        data['sub_type'] = data['sub_type'].pk

        del data['name']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_code(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, created_by=user.pk)
        data['sub_type'] = data['sub_type'].pk

        del data['code']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400
