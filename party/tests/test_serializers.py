import factory
from faker import Faker

from ..serializers import PartySubTypeSerializer, CustomerSerializer
from ..models import PartySubType, Customer
from .factory import PartySubTypeFactory, CustomerFactory

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
