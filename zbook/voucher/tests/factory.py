import factory
from faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory
from django.db.models.signals import post_save

from zbook.user.tests.factory import UserFactory
from zbook.account.tests.factory import AccountFactory
from ..models import VoucherSubType, Voucher
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


@factory.django.mute_signals(post_save)
class VoucherFactory(DjangoModelFactory):
    class Meta:
        model = Voucher

    voucher_number = fake.name()
    type = FuzzyChoice(choices=VoucherType.values.keys())
    sub_type = factory.SubFactory(VoucherSubTypeFactory)
    amount = fake.random_number(digits=5)
    description = fake.sentence()
    created_by = factory.SubFactory(UserFactory)

    @factory.post_generation
    def accounts(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for account in extracted:
                self.accounts.add(account)
        else:
            self.accounts.add(AccountFactory())
            self.accounts.add(AccountFactory())
