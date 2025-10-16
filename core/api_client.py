from urllib.parse import urlparse, parse_qs


class MockResponse:
    def __init__(self, json_data, status_code):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json


class TranslationAPIMock:
    SUPPORTED_LOCALES = {'es-ES', 'fr-FR'}
    TRANSLATIONS = {
        ('apple', 'es-ES'): 'manzana',
        ('apple', 'fr-FR'): 'pomme',
        ('dog', 'es-ES'): 'perro',
    }

    def get(self, url, params=None, **kwargs):
        query, locale = self._extract_query_locale(url, params)
        if not query or not locale:
            return MockResponse({"error": "Missing parameter"}, status_code=400)
        if locale not in self.SUPPORTED_LOCALES:
            return MockResponse({"error": "Unsupported locale"}, status_code=400)
        translation = self.TRANSLATIONS.get((query, locale))
        if translation is None:
            return MockResponse({"error": "Word not found"}, status_code=404)
        return MockResponse({"translation": translation}, status_code=200)

    @staticmethod
    def _extract_query_locale(url, params):
        if params:
            query = params.get('query')
            locale = params.get('locale')
        else:
            parsed = urlparse(url)
            query_params = parse_qs(parsed.query)
            query = query_params.get('query', [None])[0]
            locale = query_params.get('locale', [None])[0]
        return query, locale
