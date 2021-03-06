import pytest
from faker import Faker
import datetime
from django.db import IntegrityError

from zbook.account.tests.factory import AccountFactory
from ..models import PartySubType, Party, Customer, Vendor
from ..choices import PartyType, PartyGender

fake = Faker()


class TestPartySubType:

    def test_name_field(self):
        sub_type = PartySubType()
        field = sub_type._meta.get_field('name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'name'
        assert field.max_length == 128
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_code_field(self):
        sub_type = PartySubType()
        field = sub_type._meta.get_field('code')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'code'
        assert field.max_length == 128
        assert field.editable
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_label_field(self):
        sub_type = PartySubType()
        field = sub_type._meta.get_field('label')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'label'
        assert field.max_length == 128
        assert field.editable
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_type_field(self):
        sub_type = PartySubType()
        field = sub_type._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.editable
        assert not field.blank
        assert not field.null
        assert field.has_default()
        assert field.default == PartyType.Customer
        assert field.choices == PartyType.choices
        assert not field.hidden
        assert not field.unique

    def test_name_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            PartySubType.objects.create(name=None, label=fake.name(), type=PartyType.Customer, created_by=user)

    def test_created_by_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            PartySubType.objects.create(name=fake.name(), label=None, type=PartyType.Customer, created_by=None)

    def test_type_default_customer(self, user):
        sub_type = PartySubType.objects.create(name=fake.name(), created_by=user)
        assert sub_type.type == PartyType.Customer

    def test_label_is_name(self, user):
        name = fake.name()
        sub_type = PartySubType.objects.create(name=name, created_by=user)
        assert sub_type.label == name

    def test_code_is_generated_from_name(self, user):
        name = fake.name()
        sub_type = PartySubType.objects.create(name=name, created_by=user)
        assert sub_type.code == name.strip().lower().replace(' ', '-')

    def test_type_text(self, user):
        sub_type = PartySubType.objects.create(name=fake.name(), created_by=user)
        assert sub_type.type_text == sub_type.get_type_display()

    def test_create(self, user):
        sub_type = PartySubType.objects.create(name=fake.name(), created_by=user)
        instance = PartySubType.objects.get(pk=sub_type.pk)

        assert sub_type.pk == instance.pk

    def test_count(self, user):
        PartySubType.objects.create(name=fake.name(), created_by=user)
        PartySubType.objects.create(name=fake.name(), created_by=user)
        PartySubType.objects.create(name=fake.name(), created_by=user)

        count = PartySubType.objects.all()

        assert count.count() == 3

    def test_edit(self, user):
        sub_type = PartySubType.objects.create(name=fake.name(), created_by=user)
        sub_type.name = str(1234)
        sub_type.save()
        instance = PartySubType.objects.get(pk=sub_type.pk)

        assert instance.name == str(1234)

    def test_str(self, user):
        sub_type = PartySubType.objects.create(name=fake.name(), created_by=user)
        assert str(sub_type) == sub_type.name


class TestParty:

    def test_name_field(self):
        party = Party()
        field = party._meta.get_field('name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'name'
        assert field.max_length == 128
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_phone_field(self):
        party = Party()
        field = party._meta.get_field('phone')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'phone'
        assert field.max_length == 16
        assert field.editable
        assert not field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_email_field(self):
        party = Party()
        field = party._meta.get_field('email')

        assert field.__class__.__name__ == 'EmailField'
        assert field.verbose_name == 'email'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert not field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_code_field(self):
        party = Party()
        field = party._meta.get_field('code')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'code'
        assert field.max_length == 16
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_company_name_field(self):
        party = Party()
        field = party._meta.get_field('company_name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'company name'
        assert field.max_length == 128
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_address_field(self):
        party = Party()
        field = party._meta.get_field('address')

        assert field.__class__.__name__ == 'TextField'
        assert field.verbose_name == 'address'
        assert field.editable
        assert field.null
        assert field.blank
        assert field.has_default()
        assert not field.default        # Default is empty string
        assert not field.hidden
        assert not field.unique

    def test_entry_date_field(self):
        party = Party()
        field = party._meta.get_field('entry_date')

        assert field.__class__.__name__ == 'DateField'
        assert field.verbose_name == 'entry date'
        assert field.editable
        assert field.null
        assert field.blank
        assert field.has_default()
        assert field.default == datetime.date.today
        assert not field.hidden
        assert not field.unique

    def test_gender_field(self):
        party = Party()
        field = party._meta.get_field('gender')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'gender'
        assert field.editable
        assert field.null
        assert field.blank
        assert field.has_default()
        assert field.default == PartyGender.Male
        assert field.choices == PartyGender.choices
        assert not field.hidden
        assert not field.unique

    def test_account_field(self):
        from zbook.account.models import Account
        party = Party()
        field = party._meta.get_field('account')

        assert field.__class__.__name__ == 'ForeignKey'
        assert field.verbose_name == 'account'
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.remote_field.on_delete.__name__ == 'DO_NOTHING'
        assert field.remote_field.model == Account

    def test_currency_field(self):
        party = Party()
        field = party._meta.get_field('currency')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'currency'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_bank_account_name_field(self):
        party = Party()
        field = party._meta.get_field('bank_account_name')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'bank account name'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_bank_account_number_field(self):
        party = Party()
        field = party._meta.get_field('bank_account_number')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'bank account number'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_passport_field(self):
        party = Party()
        field = party._meta.get_field('passport')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'passport'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_etin_field(self):
        party = Party()
        field = party._meta.get_field('etin')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'etin'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_bin_field(self):
        party = Party()
        field = party._meta.get_field('bin')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'bin'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_vat_reg_no_field(self):
        party = Party()
        field = party._meta.get_field('vat_reg_no')

        assert field.__class__.__name__ == 'CharField'
        assert field.verbose_name == 'vat reg no'
        assert field.max_length == 64
        assert field.editable
        assert field.null
        assert field.blank
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique

    def test_type_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            Party.objects.create(created_by=user, name=None)

    def test_gender_text(self, user):
        party = Party.objects.create(created_by=user, name=fake.name())
        assert party.gender_text == party.get_gender_display()

    def test_str(self, user):
        party = Party.objects.create(created_by=user, name=fake.name())
        assert str(party) == f'{party.name}'

    def test_create(self, user):
        name = fake.name()
        account = AccountFactory(created_by=user)
        party = Party.objects.create(created_by=user, name=name, account=account)

        instance = Party.objects.get(pk=party.pk)

        assert instance.name == name
        assert instance.account == account

    def test_edit(self, user):
        name = fake.name()
        account = AccountFactory(created_by=user)
        party = Party.objects.create(created_by=user, name=fake.name(), account=account)
        party.name = name
        party.save()

        instance = Party.objects.get(pk=party.pk)

        assert instance.name == name
        assert instance.account == account

    def test_count(self, user):
        Party.objects.create(created_by=user, name=fake.name())
        Party.objects.create(created_by=user, name=fake.name())

        queryset = Party.objects.all()

        assert queryset.count() == 2


class TestCustomer:

    def test_type_field(self, db):
        party = Customer()
        field = party._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.choices == PartyType.choices
        assert field.default == PartyType.Customer
        assert field.has_default()
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.hidden
        assert not field.unique

    def test_type_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            Customer.objects.create(created_by=user, name=fake.name(), type=None)

    def test_type_default_customer(self, user):
        customer = Customer.objects.create(created_by=user, name=fake.name())
        assert customer.type == PartyType.Customer

    def test_type_text(self, user):
        customer = Customer.objects.create(created_by=user, name=fake.name())
        assert customer.type_text == customer.get_type_display()

    def test_str(self, user):
        customer = Customer.objects.create(created_by=user, name=fake.name())
        assert str(customer) == f'{customer.name} # {customer.type_text}'

    def test_create(self, user):
        name = fake.name()
        customer = Customer.objects.create(created_by=user, name=name)

        instance = Customer.objects.get(pk=customer.pk)

        assert instance.name == name
        assert instance.type == PartyType.Customer

    def test_edit(self, user):
        name = fake.name()
        customer = Customer.objects.create(created_by=user, name=fake.name())
        customer.name = name
        customer.save()

        instance = Customer.objects.get(pk=customer.pk)

        assert instance.name == name
        assert instance.type == PartyType.Customer

    def test_count(self, user):
        Customer.objects.create(created_by=user, name=fake.name())
        Customer.objects.create(created_by=user, name=fake.name())
        Customer.objects.create(created_by=user, name=fake.name())

        queryset = Customer.objects.all()

        assert queryset.count() == 3


class TestVendor:

    def test_type_field(self, db):
        party = Vendor()
        field = party._meta.get_field('type')

        assert field.__class__.__name__ == 'IntegerField'
        assert field.verbose_name == 'type'
        assert field.choices == PartyType.choices
        assert field.default == PartyType.Vendor
        assert field.has_default()
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.hidden
        assert not field.unique

    def test_type_cannot_be_null(self, user):
        with pytest.raises(IntegrityError) as error:
            Vendor.objects.create(created_by=user, name=fake.name(), type=None)

    def test_type_default_vendor(self, user):
        vendor = Vendor.objects.create(created_by=user, name=fake.name())
        assert vendor.type == PartyType.Vendor

    def test_type_text(self, user):
        vendor = Vendor.objects.create(created_by=user, name=fake.name())
        assert vendor.type_text == vendor.get_type_display()

    def test_str(self, user):
        vendor = Vendor.objects.create(created_by=user, name=fake.name())
        assert str(vendor) == f'{vendor.name} # {vendor.type_text}'

    def test_create(self, user):
        name = fake.name()
        vendor = Vendor.objects.create(created_by=user, name=name)

        instance = Vendor.objects.get(pk=vendor.pk)

        assert instance.name == name
        assert instance.type == PartyType.Vendor

    def test_edit(self, user):
        name = fake.name()
        vendor = Vendor.objects.create(created_by=user, name=fake.name())
        vendor.name = name
        vendor.save()

        instance = Vendor.objects.get(pk=vendor.pk)

        assert instance.name == name
        assert instance.type == PartyType.Vendor

    def test_count(self, user):
        Vendor.objects.create(created_by=user, name=fake.name())
        Vendor.objects.create(created_by=user, name=fake.name())
        Vendor.objects.create(created_by=user, name=fake.name())

        queryset = Vendor.objects.all()

        assert queryset.count() == 3
