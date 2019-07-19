import pytest
from faker import Faker
from django.db.utils import IntegrityError

from .factory import AccountSubTypeFactory
from ..models import AccountSubType
from ..choices import AccountType

fake = Faker()


class TestAccountSubType:

    @pytest.mark.django_db
    def test_name_max_length(self):
        sub_type = AccountSubTypeFactory()
        max_length = sub_type._meta.get_field('name').max_length
        assert max_length == 64

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
    def test_name_cannot_be_null(self):
        with pytest.raises(IntegrityError) as error:
            AccountSubType.objects.create(name=None, type=AccountType.Asset, order=0)

    @pytest.mark.django_db
    def test_type_cannot_be_null(self):
        with pytest.raises(IntegrityError) as error:
            AccountSubType.objects.create(name=fake.name(), type=None, order=0)

    @pytest.mark.django_db
    def test_order_can_be_null(self):
        sub_type = AccountSubType.objects.create(name=fake.name(), type=AccountType.Asset, order=None)
        sub_type.save()

        query = AccountSubType.objects.all()
        saved_obj = query.first()

        assert query.count() == 1
        assert saved_obj.name == sub_type.name
        assert saved_obj.type == sub_type.type
        assert saved_obj.order == None

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
