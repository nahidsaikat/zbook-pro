import pytest
from faker import Faker

from account.tests.factory import AccountSubTypeFactory
from account.models import AccountSubType
from account.choices import AccountType

fake = Faker()


class TestAccountSubType:

    @pytest.mark.django_db
    def test_create(self):
        sub_type = AccountSubType.objects.create(name=fake.name(), type=AccountType.Asset, order=0)
        sub_type.save()

        query = AccountSubType.objects.all()
        saved_obj = query.first()

        assert query.count() == 1
        assert saved_obj.name == sub_type.name
        assert saved_obj.type == sub_type.type
        assert saved_obj.order == sub_type.order

    @pytest.mark.django_db
    def test_count(self):
        AccountSubTypeFactory()
        AccountSubTypeFactory()

        query = AccountSubType.objects.all()

        assert query.count() == 2

    @pytest.mark.django_db
    def test_edit(self):
        sub_type = AccountSubType.objects.create(name=fake.name(), type=AccountType.Asset, order=0)
        sub_type.save()
        new_name = 'new name'
        sub_type.name = new_name
        sub_type.order = 1
        sub_type.save()

        saved_obj = AccountSubType.objects.first()

        assert saved_obj.name == new_name
        assert saved_obj.order == 1
