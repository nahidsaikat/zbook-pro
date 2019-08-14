import factory
from faker import Faker

from .factory import VoucherSubTypeFactory
from ..models import VoucherSubType
from ..serializers import VoucherSubTypeSerializer

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
