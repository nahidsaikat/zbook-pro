import factory
from faker import Faker
from decimal import Decimal

from .factory import VoucherSubTypeFactory, VoucherFactory
from ..models import VoucherSubType, Voucher, Ledger
from ..serializers import VoucherSubTypeSerializer, VoucherSerializer

fake = Faker()


class TestVoucherSubTypeSerailizer:

    def test_create(self, user):
        name = fake.name()
        prefix = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, name=name, prefix=prefix, created_by=user.pk)
        data['debit_account'] = data['debit_account'].pk
        data['credit_account'] = data['credit_account'].pk

        serializer = VoucherSubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name
        assert serializer.validated_data.get('prefix') == prefix

        serializer.save()

        query = VoucherSubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name
        assert sub_type.prefix == prefix

    def test_create_type_error(self):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory)
        del data['type']

        serializer = VoucherSubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_name_error(self):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory)
        del data['name']

        serializer = VoucherSubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_prefix_error(self):
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory)
        del data['prefix']

        serializer = VoucherSubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_update(self, user):
        name = fake.name()
        prefix = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VoucherSubTypeFactory, name=name, prefix=prefix, created_by=user,
                             debit_account=None, credit_account=None)
        sub_type = VoucherSubTypeFactory(created_by=user)

        serializer = VoucherSubTypeSerializer()
        serializer.update(sub_type, data)

        query = VoucherSubType.objects.all()
        saved_sub_type = query.first()

        assert query.count() == 1
        assert saved_sub_type.name == name
        assert saved_sub_type.prefix == prefix


class TestVoucherSerailizer:

    def test_create(self, user, sub_type, debit_account, credit_account):
        voucher_number = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VoucherFactory, voucher_number=voucher_number, amount=Decimal(1000),
                             created_by=user.pk, sub_type=sub_type.pk, type=sub_type.type,
                             accounts=[debit_account.pk, credit_account.pk], ledgers=[{
                            'account_id': debit_account.pk, 'amount': Decimal(1000)}, {
                            'account_id': credit_account.pk, 'amount': Decimal(-1000)}]
                             )

        serializer = VoucherSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('voucher_number') == voucher_number
        assert serializer.validated_data.get('sub_type') == sub_type

        serializer.save()

        query = Voucher.objects.all()
        voucher = query.first()

        assert query.count() == 1
        assert voucher.voucher_number == voucher_number
        assert voucher.sub_type.pk == sub_type.pk
        assert voucher.amount == Decimal(1000)

        ledger_query = Ledger.objects.all()
        assert ledger_query.count() == 2

    def test_create_sub_type_error(self, user, sub_type, debit_account, credit_account):
        data = factory.build(dict, FACTORY_CLASS=VoucherFactory, created_by=user.pk, sub_type=sub_type.pk,
                             type=sub_type.type, accounts=[debit_account.pk, credit_account.pk])
        del data['sub_type']

        serializer = VoucherSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_amount_error(self, user, sub_type, debit_account, credit_account):
        data = factory.build(dict, FACTORY_CLASS=VoucherFactory, created_by=user.pk, sub_type=sub_type.pk,
                             type=sub_type.type, accounts=[debit_account.pk, credit_account.pk])
        del data['amount']

        serializer = VoucherSerializer(data=data)
        assert not serializer.is_valid()

    def test_update(self, user, sub_type, debit_account, credit_account):
        voucher_number = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VoucherFactory, created_by=user, sub_type=sub_type,
                             voucher_number=voucher_number, accounts=[debit_account.pk, credit_account.pk])
        voucher = VoucherFactory(created_by=user)

        serializer = VoucherSerializer()
        serializer.update(voucher, data)

        query = Voucher.objects.all()
        saved_voucher = query.first()

        assert query.count() == 1
        assert saved_voucher.voucher_number == voucher_number
