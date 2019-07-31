import factory
from faker import Faker
from factory.django import DjangoModelFactory, ImageField
from django.contrib.auth import get_user_model

User = get_user_model()
fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    username = fake.name()
    first_name = fake.name()
    last_name = fake.name()
    email = factory.LazyAttribute(lambda obj: f'{fake.email()}')
    profile_picture = ImageField()
