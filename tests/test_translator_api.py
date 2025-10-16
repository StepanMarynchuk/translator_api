import pytest
import requests
from http import HTTPStatus


@pytest.mark.get_request
class TestTranslationAPIGet:

    def test_url_with_query_parameters(self, api_base_url):
        url = f"{api_base_url}?query=apple&locale=es-ES"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.OK
        assert response.json()['translation'] == 'manzana'

    def test_using_params_argument(self, api_base_url):
        response = requests.get(api_base_url, params={'query': 'apple', 'locale': 'es-ES'})
        assert response.status_code == HTTPStatus.OK
        assert response.json()['translation'] == 'manzana'

    def test_word_not_found_url(self, api_base_url):
        url = f"{api_base_url}?query=banana&locale=es-ES"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.NOT_FOUND

        assert response.json()['error'] == 'Word not found'

    def test_word_not_found_params(self, api_base_url):
        response = requests.get(api_base_url, params={'query': 'banana', 'locale': 'es-ES'})
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json()['error'] == 'Word not found'

    def test_missing_query_param(self, api_base_url):
        response = requests.get(api_base_url, params={'locale': 'es-ES'})
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json()['error'] == 'Missing parameter'

    def test_missing_locale_param(self, api_base_url):
        response = requests.get(api_base_url, params={'query': 'apple'})
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json()['error'] == 'Missing parameter'

    def test_unsupported_locale_url(self, api_base_url):
        url = f"{api_base_url}?query=apple&locale=de-DE"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json()['error'] == 'Unsupported locale'

    def test_unsupported_locale_params(self, api_base_url):
        response = requests.get(api_base_url, params={'query': 'apple', 'locale': 'de-DE'})
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json()['error'] == 'Unsupported locale'
