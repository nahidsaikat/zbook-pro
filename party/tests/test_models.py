import pytest
from faker import Faker
from django.db import IntegrityError

from ..models import PartySubType
from ..choices import PartyType

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
