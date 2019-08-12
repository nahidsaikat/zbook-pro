from django.urls import reverse, resolve


class TestAccountSubTypeUrls:

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
