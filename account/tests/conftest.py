import pytest
from .factory import AccountSubTypeFactory


@pytest.fixture
def sub_type(db):
    return AccountSubTypeFactory()
