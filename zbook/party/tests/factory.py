import factory
from faker import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from zbook.party.models import PartySubType, Customer, Vendor
from zbook.party.choices import PartyType

fake = Faker()


class PartySubTypeFactory(DjangoModelFactory):
    class Meta:
        model = PartySubType

    name = fake.name()
    label = fake.name()
    type = FuzzyChoice(choices=PartyType.values.keys())


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = fake.name()
    phone = '+8801738656117'


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    name = fake.name()
    phone = '+8801738656117'
