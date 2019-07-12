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
        saved_object = query.first()

        assert query.count() == 1
        assert saved_object.name == sub_type.name
        assert saved_object.type == sub_type.type
        assert saved_object.order == sub_type.order

    @pytest.mark.django_db
    def test_count(self):
        AccountSubTypeFactory()
        AccountSubTypeFactory()

        query = AccountSubType.objects.all()

        assert query.count() == 2
