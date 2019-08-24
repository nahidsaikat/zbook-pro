from django.urls import reverse, resolve
from .factory import VoucherSubTypeFactory, VoucherFactory


class TestVoucherSubTypeUrls:

    def test_list_create_url_reverse(self):
        url = reverse('voucher:subtype:list-create')
        assert url == '/api/v1/voucher/subtype/'

    def test_list_create_url_resolve(self):
        url = reverse('voucher:subtype:list-create')

        resolver = resolve(url)

        assert resolver.app_name == 'voucher:subtype'
        assert resolver.url_name == 'list-create'
        assert resolver.view_name == 'voucher:subtype:list-create'
        assert resolver.namespace == 'voucher:subtype'
        assert resolver.func.__name__ == 'VoucherSubTypeListCreateAPIView'

    def test_detail_update_url_reverse(self, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        url = reverse('voucher:subtype:detail-update', args=[subtype.pk])
        assert url == f'/api/v1/voucher/subtype/{subtype.pk}/'

    def test_detail_update_url_resolve(self, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        url = reverse('voucher:subtype:detail-update', args=[subtype.pk])

        resolver = resolve(url)

        assert resolver.app_name == 'voucher:subtype'
        assert resolver.url_name == 'detail-update'
        assert resolver.view_name == 'voucher:subtype:detail-update'
        assert resolver.namespace == 'voucher:subtype'
        assert resolver.func.__name__ == 'VoucherSubTypeRetrieveUpdateAPIView'


class TestVoucherUrls:

    def test_list_create_url_reverse(self):
        url = reverse('voucher:list-create')
        assert url == '/api/v1/voucher/'

    def test_list_create_url_resolve(self):
        url = reverse('voucher:list-create')

        resolver = resolve(url)

        assert resolver.app_name == 'voucher'
        assert resolver.url_name == 'list-create'
        assert resolver.view_name == 'voucher:list-create'
        assert resolver.namespace == 'voucher'
        assert resolver.func.__name__ == 'VoucherListCreateAPIView'

    def test_detail_update_url_reverse(self, user):
        subtype = VoucherSubTypeFactory(created_by=user)
        voucher = VoucherFactory(created_by=user, sub_type=subtype)
        url = reverse('voucher:detail-update', args=[voucher.pk])
        assert url == f'/api/v1/voucher/{voucher.pk}/'
