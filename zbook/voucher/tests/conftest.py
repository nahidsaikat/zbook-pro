import pytest
from faker import Faker

from zbook.account.choices import AccountType
from zbook.account.tests.factory import AccountFactory
from zbook.voucher.models import VoucherSubType

fake = Faker()


@pytest.fixture
def sub_type(self, user):
    return VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)


@pytest.fixture
def debit_account(self, user):
    return AccountFactory(type=AccountType.Asset)


@pytest.fixture
def credit_account(self, user):
    return AccountFactory(type=AccountType.Liability)
