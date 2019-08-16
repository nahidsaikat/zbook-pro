import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice
from django.urls import reverse

from zbook.voucher.choices import VoucherType
from .factory import VoucherSubTypeFactory

fake = Faker()


class TestPartySubTypeListCreateAPIView:
    url = reverse('voucher:subtype:list-create')

    def test_create(self, auth_client, user):
        name = fake.name()
        _type = FuzzyChoice(choices=VoucherType.values.keys()).fuzz()
        prefix = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, name=name, type=_type, prefix=prefix, created_by=None)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('name') == name
        assert response.data.get('prefix') == prefix
        assert response.data.get('type') == _type
        assert response.data.get('created_by') == user.pk

    def test_create_name_error(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        del data['name']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_prefix_error(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        del data['prefix']

        response = auth_client.post(self.url, data)

        assert response.status_code == 400

    def test_create_default_type_receive(self, auth_client, user):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        del data['type']

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('type') == VoucherType.Receive

    def test_create_unauthorize(self, client, user):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        response = client.post(self.url, data)

        assert response.status_code == 401

    def test_get_list(self, auth_client, user):
        VoucherSubTypeFactory(created_by=user)
        VoucherSubTypeFactory(created_by=user)
        VoucherSubTypeFactory(created_by=user)

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, user):
        VoucherSubTypeFactory(created_by=user)

        response = client.get(self.url)

        assert response.status_code == 401


class TestVoucherSubTypeRetrieveUpdateAPIView:

    def test_update(self, auth_client, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        name = fake.name()
        prefix = fake.name()
        _type = FuzzyChoice(choices=VoucherType.values.keys()).fuzz()
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, type=_type, name=name, prefix=prefix,
                             no_start_from=2000, created_by=user.pk)
        debit_account = data['debit_account'] = data['debit_account'].pk
        credit_account = data['credit_account'] = data['credit_account'].pk

        url = reverse('voucher:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('name') == name
        assert response.data.get('prefix') == prefix
        assert response.data.get('type') == _type
        assert response.data.get('debit_account') == debit_account
        assert response.data.get('credit_account') == credit_account

    def test_update_inactive(self, auth_client, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, inactive=1, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        url = reverse('voucher:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('inactive') == True

    def test_update_deleted(self, auth_client, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, deleted=1, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        url = reverse('voucher:subtype:detail-update', args=[subtype.pk])
        response = auth_client.patch(url, data)

        assert response.status_code == 200
        assert response.data.get('deleted') == True
