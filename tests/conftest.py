import pytest
from tests.helpers.api_client import ApiClient

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_client(base_url):
    return ApiClient(base_url)

@pytest.fixture(params=[1, 2, 3])  # Добавьте эту фикстуру
def valid_post_id(request):
    return request.param

@pytest.fixture
def valid_comment_data():
    return {
        "name": "Test User",
        "email": "test@example.com",
        "body": "Test content"
    }