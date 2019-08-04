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
