import pytest
import logging
from tests.helpers.api_client import ApiClient

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

@pytest.fixture(scope="module")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_client(base_url):
    return ApiClient(base_url)

@pytest.fixture(params=[1, 2, 3])
def valid_post_id(request):
    return request.param