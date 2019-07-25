from django.urls import reverse, resolve
from ..factory import AccountSubTypeFactory


class TestAccountSubTypeUrls:

    def test_list_create_url_reverse(self):
        url = reverse('account:subtype:list-create')
        assert url == '/api/v1/account/subtype/'

    def test_list_create_url_resolve(self):
        url = reverse('account:subtype:list-create')

        resolver = resolve(url)

        assert resolver.app_name == 'account:subtype'
        assert resolver.url_name == 'list-create'
        assert resolver.view_name == 'account:subtype:list-create'
        assert resolver.namespace == 'account:subtype'
        assert resolver.func.__name__ == 'AccountSubTypeListCreateAPIView'

    def test_detail_update_url_reverse(self, db):
        subtype = AccountSubTypeFactory()
        url = reverse('account:subtype:detail-update', args=[subtype.pk])
        assert url == '/api/v1/account/subtype/1/'

    def test_detail_update_url_resolve(self, db):
        subtype = AccountSubTypeFactory()
        url = reverse('account:subtype:detail-update', args=[subtype.pk])

        resolver = resolve(url)

        assert resolver.app_name == 'account:subtype'
        assert resolver.url_name == 'detail-update'
        assert resolver.view_name == 'account:subtype:detail-update'
        assert resolver.namespace == 'account:subtype'
        assert resolver.func.__name__ == 'AccountSubTypeRetrieveUpdateAPIView'