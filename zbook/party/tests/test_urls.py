from django.urls import reverse, resolve
from .factory import PartySubTypeFactory, CustomerFactory


class TestPartySubTypeUrls:

    def test_list_create_url_reverse(self):
        url = reverse('party:subtype:list-create')
        assert url == '/api/v1/party/subtype/'

    def test_list_create_url_resolve(self):
        url = reverse('party:subtype:list-create')

        resolver = resolve(url)

        assert resolver.app_name == 'party:subtype'
        assert resolver.url_name == 'list-create'
        assert resolver.view_name == 'party:subtype:list-create'
        assert resolver.namespace == 'party:subtype'
        assert resolver.func.__name__ == 'PartySubTypeListCreateAPIView'

    def test_detail_update_url_reverse(self, user):
        subtype = PartySubTypeFactory(created_by=user)
        url = reverse('party:subtype:detail-update', args=[subtype.pk])
        assert url == f'/api/v1/party/subtype/{subtype.pk}/'

    def test_detail_update_url_resolve(self, user):
        subtype = PartySubTypeFactory(created_by=user)
        url = reverse('party:subtype:detail-update', args=[subtype.pk])

        resolver = resolve(url)

        assert resolver.app_name == 'party:subtype'
        assert resolver.url_name == 'detail-update'
        assert resolver.view_name == 'party:subtype:detail-update'
        assert resolver.namespace == 'party:subtype'
        assert resolver.func.__name__ == 'PartySubTypeRetrieveUpdateAPIView'


class TestCustomerUrls:

    def test_list_create_url_reverse(self):
        url = reverse('party:customer:list-create')
        assert url == '/api/v1/party/customer/'

    def test_list_create_url_resolve(self):
        url = reverse('party:customer:list-create')

        resolver = resolve(url)

        assert resolver.app_name == 'party:customer'
        assert resolver.url_name == 'list-create'
        assert resolver.view_name == 'party:customer:list-create'
        assert resolver.namespace == 'party:customer'
        assert resolver.func.__name__ == 'CustomerListCreateAPIView'

    def test_detail_update_url_reverse(self, user):
        customer = CustomerFactory(created_by=user)
        url = reverse('party:customer:detail-update', args=[customer.pk])
        assert url == f'/api/v1/party/customer/{customer.pk}/'
