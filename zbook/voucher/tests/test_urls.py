from django.urls import reverse


class TestPartySubTypeUrls:

    def test_list_create_url_reverse(self):
        url = reverse('voucher:subtype:list-create')
        assert url == '/api/v1/voucher/subtype/'
