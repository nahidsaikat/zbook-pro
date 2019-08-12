from django.urls import reverse


class TestAccountSubTypeUrls:

    def test_list_create_url_reverse(self):
        url = reverse('party:subtype:list-create')
        assert url == '/api/v1/party/subtype/'
