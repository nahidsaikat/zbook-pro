from django.urls import reverse, resolve


class TestPartySubTypeUrls:

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
