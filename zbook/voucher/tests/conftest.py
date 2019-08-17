import pytest
from faker import Faker

from zbook.account.choices import AccountType
from zbook.account.tests.factory import AccountFactory
from zbook.voucher.models import VoucherSubType
from zbook.voucher.tests.factory import VoucherFactory

fake = Faker()


@pytest.fixture
def sub_type(user):
    return VoucherSubType.objects.create(name=fake.name(), prefix=fake.name(), created_by=user)


@pytest.fixture
def debit_account(user):
    return AccountFactory(name=fake.name(), code=fake.random_int(1, 100), type=AccountType.Asset)


@pytest.fixture
def credit_account(user):
    return AccountFactory(name=fake.name(), code=fake.random_int(1, 100), type=AccountType.Liability)


@pytest.fixture
def voucher(user, debit_account, credit_account):
    return VoucherFactory(accounts=[debit_account, credit_account], created_by=user)
