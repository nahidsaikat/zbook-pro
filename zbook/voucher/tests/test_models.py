import pytest
from faker import Faker
from django.db import IntegrityError

from ..models import VoucherSubType
from ..choices import VoucherType

fake = Faker()


class TestVoucherSubType:

    def test_name_field(self, db):
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'name'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_type_field(self):
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.editable
        assert not field.blank
        assert not field.null
        assert field.has_default()
        assert field.default == VoucherType.Receive
        assert field.choices == VoucherType.choices
        assert not field.hidden
        assert not field.unique

    def test_prefix_field(self, db):
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('prefix')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'prefix'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_no_start_from_field(self):
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('no_start_from')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'no start from'
        assert field.editable
        assert field.blank
        assert field.null
        assert field.has_default()
        assert field.default == 1000
        assert not field.hidden
        assert not field.unique

    def test_debit_account_field(self):
        from zbook.account.models import Account
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('debit_account')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'debit account'
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Account
        assert field.remote_field.related_name == 'voucher_sub_type_debit_account'

    def test_credit_account_field(self):
        from zbook.account.models import Account
        sub_type = VoucherSubType()
        field = sub_type._meta.get_field('credit_account')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'credit account'
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Account
        assert field.remote_field.related_name == 'voucher_sub_type_credit_account'

    def test_name_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            VoucherSubType.objects.create(name=None, prefix=fake.name(), type=VoucherType.Payment, created_by=user)

    def test_prefix_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            VoucherSubType.objects.create(name=fake.name(), prefix=None, type=VoucherType.Payment, created_by=user)
