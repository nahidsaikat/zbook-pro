import random
import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from user.tests.factory import UserFactory
from account.models import AccountSubType, Account
from account.choices import AccountType

fake = Faker()


class AccountSubTypeFactory(DjangoModelFactory):
    class Meta:
        model = AccountSubType

    name = fake.name()
    type = FuzzyChoice(choices=AccountType.values.keys())
    order = random.randint(0, 10)
    created_by = factory.SubFactory(UserFactory)


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    name = fake.name()
    code = fake.random_int(1, 100)
    type = FuzzyChoice(choices=AccountType.values.keys())
    sub_type = factory.SubFactory(AccountSubTypeFactory)
    depth = random.randint(0, 10)
    entry_date = fake.date()
    description = fake.sentence()
    created_by = factory.SubFactory(UserFactory)
