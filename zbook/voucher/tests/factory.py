import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from zbook.account.tests.factory import AccountFactory
from zbook.user.tests.factory import UserFactory
from ..models import VoucherSubType
from ..choices import VoucherType

fake = Faker()


class VoucherSubTypeFactory(DjangoModelFactory):
    class Meta:
        model = VoucherSubType

    type = FuzzyChoice(choices=VoucherType.values.keys())
    name = fake.name()
    prefix = fake.name()
    debit_account = factory.SubFactory(AccountFactory)
    credit_account = factory.SubFactory(AccountFactory)
    created_by = factory.SubFactory(UserFactory)
