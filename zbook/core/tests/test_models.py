from faker import Faker

from ..models import Location

fake = Faker()


class TestAccountSubType:

    def test_name_field(self, db):
        location = Location()
        field = location._meta.get_field('name')
        assert field.verbose_name == 'name'
        assert field.max_length == 64
        assert field.editable
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique
