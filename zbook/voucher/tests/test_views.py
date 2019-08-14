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
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, name=name, type=_type, prefix=prefix)
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
