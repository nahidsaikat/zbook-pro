import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from zbook.user.tests.factory import UserFactory
from zbook.core.models import Location
from zbook.core.choices import LocationType

fake = Faker()


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = fake.name()
    code = fake.name()
    type = FuzzyChoice(choices=LocationType.values.keys())
    created_by = factory.SubFactory(UserFactory)
