import factory
from faker import Faker

from ..serializers import PartySubTypeSerializer, CustomerSerializer, VendorSerializer
from ..models import PartySubType, Customer, Vendor
from .factory import PartySubTypeFactory, CustomerFactory, VendorFactory

fake = Faker()


class TestPartySubTypeSerializer:

    def test_create(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory,
                             name=name,
                             created_by=user.pk)

        serializer = PartySubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = PartySubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name

    def test_create_name_error(self):
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory)
        del data['name']

        serializer = PartySubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_type_error(self):
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory)
        del data['type']

        serializer = PartySubTypeSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_code_auto_generated(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, name=name, created_by=user.pk)

        serializer = PartySubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = PartySubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name
        assert sub_type.code == str(name).strip().lower().replace(' ', '-')

    def test_create_set_label(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, name=name, created_by=user.pk)
        del data['label']

        serializer = PartySubTypeSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = PartySubType.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name
        assert sub_type.label == name

    def test_update(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=PartySubTypeFactory, name=name, created_by=user)
        sub_type = PartySubTypeFactory(created_by=user)

        serializer = PartySubTypeSerializer()
        serializer.update(sub_type, data)

        query = PartySubType.objects.all()
        saved_sub_type = query.first()

        assert query.count() == 1
        assert saved_sub_type.name == name


class TestCustomerSerializer:

    def test_create(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=CustomerFactory,
                             name=name,
                             created_by=user.pk)

        serializer = CustomerSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = Customer.objects.all()
        sub_type = query.first()

        assert query.count() == 1
        assert sub_type.name == name

    def test_create_name_error(self, user):
        data = factory.build(dict, FACTORY_CLASS=CustomerFactory, created_by=user)
        del data['name']

        serializer = CustomerSerializer(data=data)
        assert not serializer.is_valid()

    def test_create_phone_error(self, user):
        data = factory.build(dict, FACTORY_CLASS=CustomerFactory, created_by=user)
        del data['phone']

        serializer = CustomerSerializer(data=data)
        assert not serializer.is_valid()

    def test_update(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=CustomerFactory, name=name, created_by=user)
        customer = CustomerFactory(created_by=user)

        serializer = CustomerSerializer()
        serializer.update(customer, data)

        query = Customer.objects.all()
        saved_customer = query.first()

        assert query.count() == 1
        assert saved_customer.name == name


class TestVendorSerializer:

    def test_create(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VendorFactory, name=name, created_by=user.pk)

        serializer = VendorSerializer(data=data)
        serializer.is_valid()

        assert serializer.validated_data.get('name') == name

        serializer.save()

        query = Vendor.objects.all()
        vendor = query.first()

        assert query.count() == 1
        assert vendor.name == name

    def test_create_name_error(self, user):
        data = factory.build(dict, FACTORY_CLASS=VendorFactory, created_by=user)
        del data['name']

        serializer = VendorSerializer(data=data)
        assert not serializer.is_valid()

    def test_update(self, user):
        name = fake.name()
        data = factory.build(dict, FACTORY_CLASS=VendorFactory, name=name, created_by=user)
        customer = VendorFactory(created_by=user)

        serializer = VendorSerializer()
        serializer.update(customer, data)

        query = Vendor.objects.all()
        saved_vendor = query.first()

        assert query.count() == 1
        assert saved_vendor.name == name
