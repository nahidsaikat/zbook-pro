import os
import pytest
from faker import Faker

from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()
fake = Faker()


class TestUser:

    def test_meta_info(self):
        assert User.__name__ == 'User'
        assert User.USERNAME_FIELD == 'email'
        assert User.EMAIL_FIELD == 'email'
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

    def test_is_active_field(self):
        user = User()
        field = user._meta.get_field('is_active')
        assert field.name == 'is_active'
        assert field.verbose_name == 'active'
        assert not field.blank
        assert not field.null
        assert field.has_default()
        assert field.default
        assert not field.hidden
        assert not field.unique

    def test_is_staff_field(self):
        user = User()
        field = user._meta.get_field('is_staff')
        assert field.name == 'is_staff'
        assert field.verbose_name == 'staff status'
        assert not field.blank
        assert not field.null
        assert field.has_default()
        assert not field.default
        assert not field.hidden
        assert not field.unique

    def test_profile_picture_field(self):
        user = User()
        field = user._meta.get_field('profile_picture')
        assert field.name == 'profile_picture'
        assert field.get_attname() == 'profile_picture'
        assert field.verbose_name == 'profile picture'
        assert field.blank
        assert field.null
        assert not field.has_default()
        assert field.default.__name__ == 'NOT_PROVIDED'
        assert not field.hidden
        assert not field.unique
        assert field.upload_to == 'profile_picture/'

    def test_create(self, db):
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()

        queryset = User.objects.all()

        assert queryset.count() == 1
        assert queryset.first().email == user.email
        assert queryset.first().first_name == user.first_name
        assert queryset.first().last_name == user.last_name

    def test_update(self, db):
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()
        username = fake.name()
        user.username = username
        user.save()

        queryset = User.objects.all()

        assert queryset.count() == 1
        assert queryset.first().email == user.email
        assert queryset.first().first_name == user.first_name
        assert queryset.first().last_name == user.last_name
        assert queryset.first().username == username

    def test_count(self, db):
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()

        queryset = User.objects.all()

        assert queryset.count() == 2

    def test_email_is_unique(self, db):
        email = fake.email()
        User.objects.create(email=email, first_name=fake.name(), last_name=fake.name())
        with pytest.raises(IntegrityError) as error:
            User.objects.create(email=email, first_name=fake.name(), last_name=fake.name())

    def test_email_cannot_be_null(self, db):
        with pytest.raises(IntegrityError) as error:
            User.objects.create(email=None, first_name=fake.name(), last_name=fake.name())

    def test_first_name_cannot_be_null(self, db):
        with pytest.raises(IntegrityError) as error:
            User.objects.create(email=fake.email(), first_name=None, last_name=fake.name())

    def test_last_name_cannot_be_null(self, db):
        with pytest.raises(IntegrityError) as error:
            User.objects.create(email=fake.email(), first_name=fake.name(), last_name=None)

    def test_default_values(self, db):
        user = User.objects.create(email=fake.email(), first_name=fake.name(), last_name=fake.name())

        assert user.date_joined
        assert user.is_active
        assert not user.is_staff

    def test_profile_picture(self, db):
        user = User.objects.create(email=fake.email(), first_name=fake.name(), last_name=fake.name())

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        file_name = 'test_picture.gif'

        user.profile_picture = SimpleUploadedFile(file_name, small_gif, content_type='image/gif')
        user.save()

        assert user.profile_picture.name == f'profile_picture/{file_name}'
        assert user.profile_picture.path == os.path.join(settings.MEDIA_ROOT, 'profile_picture', file_name)
        user.profile_picture.delete()

    def test_get_full_name(self, db):
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()

        assert user.get_full_name() == f'{user.first_name} {user.last_name}'

    def test_get_short_name(self, db):
        user = User(
            email=fake.email(),
            first_name=fake.name(),
            last_name=fake.name(),
        )
        user.save()

        assert user.get_short_name() == f'{user.first_name}'

    def test_email_user(self):
        """TODO: need to implement this test when email configuration is done for the project"""
        assert 1 == 1
