from django.contrib.auth import get_user_model

User = get_user_model()


class TestUser:

    def test_meta_info(self):
        assert User.__name__ == 'User'
        assert User.USERNAME_FIELD == 'email'
        assert not User.REQUIRED_FIELDS
        assert User._meta.verbose_name == 'user'
        assert User._meta.verbose_name_plural == 'users'

    def test_username_field(self):
        user = User()
        field = user._meta.get_field('username')
        assert field.verbose_name == 'user name'
        assert field.max_length == 128
        assert field.blank
        assert field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_email_field(self):
        user = User()
        field = user._meta.get_field('email')
        assert field.verbose_name == 'email address'
        assert field.max_length == 254
        assert field.unique
        assert not field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden

    def test_first_name_field(self):
        user = User()
        field = user._meta.get_field('first_name')
        assert field.verbose_name == 'first name'
        assert field.max_length == 30
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_last_name_field(self):
        user = User()
        field = user._meta.get_field('last_name')
        assert field.name == 'last_name'
        assert field.verbose_name == 'last name'
        assert field.max_length == 30
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique

    def test_date_joined_field(self):
        user = User()
        field = user._meta.get_field('date_joined')
        assert field.name == 'date_joined'
        assert field.verbose_name == 'date joined'
        assert field.auto_now_add
        assert not field.auto_now
        assert field.blank
        assert not field.null
        assert not field.has_default()
        assert not field.hidden
        assert not field.unique
