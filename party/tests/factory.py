import factory
from faker import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from party.models import PartySubType
from party.choices import PartyType

fake = Faker()


class PartySubTypeFactory(DjangoModelFactory):
    class Meta:
        model = PartySubType

    name = fake.name()
    label = fake.name()
    type = FuzzyChoice(choices=PartyType.values.keys())
