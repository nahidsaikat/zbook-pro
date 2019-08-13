from ..models import VoucherSubType
from ..choices import VoucherType


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
