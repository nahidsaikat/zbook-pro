import datetime
import pytest
from faker import Faker
from decimal import Decimal
from django.db import IntegrityError

from zbook.account.choices import AccountType
from zbook.account.tests.factory import AccountFactory
from zbook.account.models import Account
from zbook.party.tests.factory import CustomerFactory
from zbook.party.models import Party
from ..models import VoucherSubType, Voucher, Ledger
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

    def test_type_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), type=None, created_by=user)

    def test_type_default_receive(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        assert sub_type.type == VoucherType.Receive

    def test_no_start_from_default_1000(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        assert sub_type.no_start_from == 1000

    def test_str(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        assert str(sub_type) == f'{sub_type.name} # {sub_type.type_text}'

    def test_type_text(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        assert sub_type.type_text == sub_type.get_type_display()

    def test_create(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), created_by=user)
        instance = VoucherSubType.objects.get(pk=sub_type.pk)

        assert sub_type.pk == instance.pk

    def test_edit(self, user):
        sub_type = VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        sub_type.name = str(1234)
        sub_type.save()
        instance = VoucherSubType.objects.get(pk=sub_type.pk)

        assert instance.name == str(1234)

    def test_count(self, user):
        VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)
        VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)

        count = VoucherSubType.objects.all()

        assert count.count() == 3


class TestVoucher:

    def test_voucher_number_field(self, db):
        voucher = Voucher()
        field = voucher._meta.get_field('voucher_number')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'voucher number'
        assert field.max_length == 64
        assert field.editable
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_entry_date_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('voucher_date')

        assert field.__class__.__name__ == 'DateField'
        assert field.verbose_name == 'voucher date'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert field.has_default()
        assert field.default == datetime.date.today
        assert not field.hidden
        assert not field.unique

    def test_type_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.editable
        assert field.blank
        assert field.null
        assert field.has_default()
        assert field.default == VoucherType.Receive
        assert field.choices == VoucherType.choices
        assert not field.hidden
        assert not field.unique

    def test_sub_type_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('sub_type')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'sub type'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == VoucherSubType

    def test_amount_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('amount')

        assert field.__class__.__name__ == 'DecimalField'
        assert field.verbose_name == 'amount'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.max_digits == 15
        assert field.decimal_places == 6

    def test_party_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('party')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'party'
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Party

    def test_ref_voucher_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('ref_voucher')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'ref voucher'
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Voucher

    def test_description_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('description')

        assert field.__class__.__name__ == 'TextField'
        assert field.verbose_name == 'description'
        assert field.editable
        assert field.null
        assert field.blank
        assert field.has_default()
        assert not field.default        # Default is empty string
        assert not field.hidden
        assert not field.unique

    def test_accounts_field(self):
        voucher = Voucher()
        field = voucher._meta.get_field('accounts')

        assert field.__class__.__name__ == 'ManyToManyField'
        assert field.verbose_name == 'accounts'
        assert field.get_attname() == 'accounts'
        assert field.editable
        assert field.many_to_many
        assert not field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.target_field.__class__.__name__ == 'AutoField'
        assert field.remote_field.model == Account
        assert field.related_model == Account
        assert field.m2m_column_name() == 'voucher_id'
        assert field.m2m_reverse_name() == 'account_id'
        assert field.m2m_db_table() == 'voucher_voucher_accounts'

    def test_voucher_number_cannot_be_null(self, user, sub_type):
        with pytest.raises(IntegrityError) as error:
            Voucher.objects.create(voucher_number=None, type=VoucherType.Payment, sub_type=sub_type,
                                   amount=Decimal(100), created_by=user)

    def test_voucher_date_cannot_be_null(self, user, sub_type):
        with pytest.raises(IntegrityError) as error:
            Voucher.objects.create(voucher_number=fake.name(), voucher_date=None, type=VoucherType.Payment,
                                   sub_type=sub_type, amount=Decimal(100), created_by=user)

    def test_sub_type_cannot_be_null(self, user, sub_type):
        with pytest.raises(IntegrityError) as error:
            Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=None,
                                   amount=Decimal(100), created_by=user)

    def test_amount_cannot_be_null(self, user, sub_type):
        with pytest.raises(IntegrityError) as error:
            Voucher.objects.create(voucher_number=None, type=VoucherType.Payment, sub_type=sub_type,
                                   amount=None, created_by=user)

    def test_accounts_cannot_be_null(self, user, sub_type):
        with pytest.raises(TypeError) as error:
            voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   amount=Decimal(100), created_by=user)
            voucher.accounts.set(None)

    def test_type_text(self, user, sub_type):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   amount=Decimal(100), created_by=user)
        assert voucher.type_text == voucher.get_type_display()

    def test_str(self, user, sub_type):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   amount=Decimal(100), created_by=user)
        assert str(voucher) == f'{voucher.voucher_number} # {voucher.type_text}'

    def test_sub_type_text(self, user, sub_type):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   amount=Decimal(100), created_by=user)
        assert voucher.sub_type_text == sub_type.name

    def test_party_name(self, user, sub_type):
        customer = CustomerFactory(created_by=user)
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   party=customer, amount=Decimal(100), created_by=user)
        assert voucher.party_name == customer.name

    def test_ref_voucher_number(self, user, sub_type):
        customer = CustomerFactory(created_by=user)
        ref_voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                   party=customer, amount=Decimal(100), created_by=user)
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                         ref_voucher=ref_voucher, party=customer, amount=Decimal(100), created_by=user)
        assert voucher.ref_voucher_number == ref_voucher.voucher_number

    def test_accounts_name(self, user, sub_type, debit_account, credit_account):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                         amount=Decimal(100), created_by=user)
        voucher.accounts.add(debit_account)
        voucher.accounts.add(credit_account)
        assert voucher.accounts_name == ', '.join([account.name for account in voucher.accounts.all()])

    def test_create(self, user, sub_type):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                         amount=Decimal(100), created_by=user)
        instance = Voucher.objects.get(pk=sub_type.pk)

        assert voucher.pk == instance.pk

    def test_edit(self, user, sub_type):
        voucher = Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                                         amount=Decimal(100), created_by=user)
        voucher.voucher_number = str(1234)
        voucher.save()
        instance = Voucher.objects.get(pk=voucher.pk)

        assert instance.voucher_number == str(1234)

    def test_count(self, user, sub_type):
        Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                               amount=Decimal(100), created_by=user)
        Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                               amount=Decimal(100), created_by=user)
        Voucher.objects.create(voucher_number=fake.name(), type=VoucherType.Payment, sub_type=sub_type,
                               amount=Decimal(100), created_by=user)

        count = Voucher.objects.all()

        assert count.count() == 3


class TestLedger:

    def test_voucher_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('voucher')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'voucher'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'CASCADE'
        assert field.remote_field.model == Voucher

    def test_account_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('account')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'account'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Account

    def test_entry_date_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('entry_date')

        assert field.__class__.__name__ == 'DateField'
        assert field.verbose_name == 'entry date'
        assert field.editable
        assert not field.null
        assert field.blank
        assert field.has_default()
        assert field.default == datetime.date.today
        assert not field.hidden
        assert not field.unique

    def test_amount_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('amount')

        assert field.__class__.__name__ == 'DecimalField'
        assert field.verbose_name == 'amount'
        assert field.editable
        assert not field.null
        assert not field.blank
        assert field.has_default()
        assert field.default == 0
        assert not field.hidden
        assert not field.unique
        assert field.max_digits == 15
        assert field.decimal_places == 6

    def test_account_amount_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('account_amount')

        assert field.__class__.__name__ == 'DecimalField'
        assert field.verbose_name == 'account amount'
        assert field.editable
        assert not field.null
        assert field.blank
        assert field.has_default()
        assert field.default == 0
        assert not field.hidden
        assert not field.unique
        assert field.max_digits == 15
        assert field.decimal_places == 6

    def test_description_field(self):
        ledger = Ledger()
        field = ledger._meta.get_field('description')

        assert field.__class__.__name__ == 'TextField'
        assert field.verbose_name == 'description'
        assert field.editable
        assert field.null
        assert field.blank
        assert field.has_default()
        assert not field.default        # Default is empty string
        assert not field.hidden
        assert not field.unique

    def test_voucher_cannot_be_null(self, user, debit_account):
        with pytest.raises(IntegrityError) as error:
            Ledger.objects.create(voucher=None, account=debit_account, amount=Decimal(1000), created_by=user)

    def test_account_cannot_be_null(self, user, voucher):
        with pytest.raises(IntegrityError) as error:
            Ledger.objects.create(voucher=voucher, account=None, amount=Decimal(1000), created_by=user)

    def test_entry_date_cannot_be_null(self, user, voucher, debit_account):
        with pytest.raises(IntegrityError) as error:
            Ledger.objects.create(voucher=voucher, account=debit_account, entry_date=None, amount=Decimal(1000), created_by=user)

    def test_amount_cannot_be_null(self, user, voucher, debit_account):
        with pytest.raises(IntegrityError) as error:
            Ledger.objects.create(voucher=voucher, account=debit_account, amount=None, created_by=user)

    def test_account_amount_set_automatically(self, user, voucher, debit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        assert ledger.amount == ledger.account_amount

    def test_str(self, user, voucher, debit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        assert str(ledger) == f'{ledger.voucher.voucher_number} # {ledger.voucher.voucher_number} # {ledger.account.name} # {ledger.amount}'

    def test_other_accounts(self, user, voucher, debit_account, credit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        assert ledger.other_accounts.first() == credit_account

    def test_other_accounts_name(self, user, voucher, debit_account, credit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        assert ledger.other_accounts_name == [credit_account.name]

    def test_create(self, user, voucher, debit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        instance = Ledger.objects.get(pk=ledger.pk)

        assert ledger.pk == instance.pk

    def test_edit(self, user, voucher, debit_account):
        ledger = Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        ledger.amount = voucher.amount
        ledger.save()

        instance = Ledger.objects.get(pk=ledger.pk)

        assert instance.amount == voucher.amount

    def test_count(self, user, voucher, debit_account):
        Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)
        Ledger.objects.create(voucher=voucher, account=debit_account, amount=Decimal(1000), created_by=user)

        count = Ledger.objects.all()

        assert count.count() == 3
