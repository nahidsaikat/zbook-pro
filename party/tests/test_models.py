from ..models import PartySubType


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
