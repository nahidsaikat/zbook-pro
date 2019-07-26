import pytest
from faker import Faker
from django.contrib.auth import get_user_model

from ...managers import UserManager

User = get_user_model()
fake = Faker()


class TestUserManager:
    manager = UserManager()
    manager.model = User

    def test_create_user(self, db):
        assert self.manager.__class__.__name__ == 'UserManager'
        first_name = fake.name()
        last_name = fake.name()
        email = fake.email()
        password = fake.password()

        user = self.manager.create_user(email=email, password=password, first_name=first_name, last_name=last_name)

        assert not user.is_superuser
        assert user.is_active
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.check_password(password)

    def test_create_user_superuser(self, db):
        user = self.manager.create_user(email=fake.email(), password=fake.password(),
                                        first_name=fake.name(), last_name=fake.name(), is_superuser=True)
        assert user.is_superuser

    def test_create_user_value_error_email(self, db):
        with pytest.raises(ValueError) as error:
            self.manager.create_user(email=None, password=fake.password())

    def test_create_superuser(self, db):
        assert self.manager.__class__.__name__ == 'UserManager'
        first_name = fake.name()
        last_name = fake.name()
        email = fake.email()
        password = fake.password()

        user = self.manager.create_superuser(email=email, password=password, first_name=first_name, last_name=last_name)

        assert user.is_superuser
        assert user.is_active
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.check_password(password)

    def test_create_superuser_value_error_email(self, db):
        with pytest.raises(ValueError) as error:
            self.manager.create_superuser(email=None, password=fake.password())

    def test_create_superuser_value_error_is_superuser(self, db):
        with pytest.raises(ValueError) as error:
            self.manager.create_superuser(email=fake.email(), password=fake.password(), is_superuser=False)
