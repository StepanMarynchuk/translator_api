import pytest
import configparser
from unittest.mock import patch
from core.api_client import TranslationAPIMock


@pytest.fixture(scope='session')
def api_base_url():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['api_base_url']


@pytest.fixture(autouse=True)
def patch_requests_get():
    """Automatically patch requests.get for all tests."""
    api_mock = TranslationAPIMock()
    with patch('requests.get', side_effect=api_mock.get):
        yield
