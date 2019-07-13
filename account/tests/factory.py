import random
from faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from account.models import AccountSubType, Account
from account.choices import AccountType

fake = Faker()


class AccountSubTypeFactory(DjangoModelFactory):
    class Meta:
        model = AccountSubType

    name = fake.name()
    type = FuzzyChoice(choices=AccountType.values.keys())
    order = random.randint(0, 10)
