import pytest
from faker import Faker
from django.db.utils import IntegrityError

from ..factory import AccountSubTypeFactory
from ...models import AccountSubType
from ...choices import AccountType

fake = Faker()


class TestAccountSubType:

    def test_name_field(self, db):
        sub_type = AccountSubType()
        field = sub_type._meta.get_field('name')
        assert field.verbose_name == 'name'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_type_field(self, db):
        sub_type = AccountSubType()
        field = sub_type._meta.get_field('type')
        assert field.verbose_name == 'type'
        assert field.choices == AccountType.choices
        assert field.default == AccountType.Asset
        assert field.has_default()
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.hidden
        assert not field.unique

    def test_order_field(self, db):
        sub_type = AccountSubType()
        field = sub_type._meta.get_field('order')
        assert field.verbose_name == 'order'
        assert field.default == 0
        assert field.has_default()
        assert field.editable
        assert field.blank
        assert field.null
        assert not field.hidden
        assert not field.unique

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
        assert not saved_obj.order

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

    def test_str(self, db):
        sub_type = AccountSubType.objects.create(name=fake.name(), type=AccountType.Asset, order=0)
        assert str(sub_type) == f'{sub_type.name}#{sub_type.get_type_display()}#{sub_type.order}'
