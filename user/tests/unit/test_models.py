from django.contrib.auth import get_user_model

User = get_user_model()


class TestUser:

    def test_meta_info(self):
        assert User.__name__ == 'User'
        assert User.USERNAME_FIELD == 'email'
        assert not User.REQUIRED_FIELDS
        assert User._meta.verbose_name == 'user'
        assert User._meta.verbose_name_plural == 'users'
