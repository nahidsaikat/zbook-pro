from ...models import BaseModel


class TestBaseModel:

    def test_abstract(self):
        base = BaseModel()
        assert base._meta.abstract

    def test_created_by(self):
        base = BaseModel()
        field = base._meta.get_field('created_by')
        assert field.name == 'created_by'
        assert field.verbose_name == 'created by'
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_updated_by(self):
        base = BaseModel()
        field = base._meta.get_field('updated_by')
        assert field.name == 'updated_by'
        assert field.verbose_name == 'updated by'
        assert field.blank
        assert field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_created_at(self):
        base = BaseModel()
        field = base._meta.get_field('created_at')
        assert field.name == 'created_at'
        assert field.verbose_name == 'created at'
        assert field.blank
        assert field.null
        assert field.auto_now_add
        assert not field.auto_now
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_updated_at(self):
        base = BaseModel()
        field = base._meta.get_field('updated_at')
        assert field.name == 'updated_at'
        assert field.verbose_name == 'updated at'
        assert field.blank
        assert field.null
        assert field.auto_now
        assert not field.auto_now_add
        assert not field.has_default()
        assert not field.unique

    def test_inactive(self):
        base = BaseModel()
        field = base._meta.get_field('inactive')
        assert field.name == 'inactive'
        assert field.verbose_name == 'inactive'
        assert field.blank
        assert field.null
        assert field.has_default()
        assert not field.default
        assert not field.hidden
        assert not field.unique

    def test_deleted(self):
        base = BaseModel()
        field = base._meta.get_field('deleted')
        assert field.name == 'deleted'
        assert field.verbose_name == 'deleted'
        assert field.blank
        assert field.null
        assert field.has_default()
        assert not field.default
        assert not field.hidden
        assert not field.unique
