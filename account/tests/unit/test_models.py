import pytest
from faker import Faker
from django.db.utils import IntegrityError
from django.urls import reverse

from ..factory import AccountSubTypeFactory
from ...models import AccountSubType, Account
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

    def test_name_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            AccountSubType.objects.create(created_by=user, name=None, type=AccountType.Asset, order=0)

    def test_type_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            AccountSubType.objects.create(created_by=user, name=fake.name(), type=None, order=0)

    def test_order_can_be_null(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=None)
        sub_type.save()

        query = AccountSubType.objects.all()
        saved_obj = query.first()

        assert query.count() == 1
        assert saved_obj.name == sub_type.name
        assert saved_obj.type == sub_type.type
        assert not saved_obj.order

    def test_create(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=0)
        sub_type.save()

        query = AccountSubType.objects.all()
        saved_obj = query.first()

        assert query.count() == 1
        assert saved_obj.name == sub_type.name
        assert saved_obj.type == sub_type.type
        assert saved_obj.order == sub_type.order

    def test_count(self, user):
        AccountSubTypeFactory(created_by=user)
        AccountSubTypeFactory(created_by=user)

        query = AccountSubType.objects.all()

        assert query.count() == 2

    def test_edit(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=0)
        sub_type.save()
        new_name = 'new name'
        sub_type.name = new_name
        sub_type.order = 1
        sub_type.save()

        saved_obj = AccountSubType.objects.first()

        assert saved_obj.name == new_name
        assert saved_obj.order == 1

    def test_str(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=0)
        assert str(sub_type) == f'{sub_type.name}#{sub_type.get_type_display()}#{sub_type.order}'

    def test_type_text(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=0)
        assert sub_type.type_text == sub_type.get_type_display()

    def test_get_absolute_url(self, user):
        sub_type = AccountSubType.objects.create(created_by=user, name=fake.name(), type=AccountType.Asset, order=0)
        assert sub_type.get_absolute_url() == reverse('account:subtype:detail-update', args=[sub_type.pk])


class TestAccount:

    def test_name_field(self, db):
        account = Account()
        field = account._meta.get_field('name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'name'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_code_field(self, db):
        account = Account()
        field = account._meta.get_field('code')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'code'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_type_field(self, db):
        account = Account()
        field = account._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.editable
        assert field.blank
        assert field.has_default()
        assert field.choices == AccountType.choices
        assert field.default == AccountType.Asset
        assert not field.null
        assert not field.hidden
        assert not field.unique

    def test_sub_type_field(self, db):
        account = Account()
        field = account._meta.get_field('sub_type')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'sub type'
        assert field.editable
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.null
        assert not field.hidden
        assert not field.unique

    def test_depth_field(self, db):
        account = Account()
        field = account._meta.get_field('depth')
        assert field.verbose_name == 'depth'
        assert field.default == 0
        assert field.has_default()
        assert field.editable
        assert field.blank
        assert field.null
        assert not field.hidden
        assert not field.unique
