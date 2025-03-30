import pytest

def test_get_comments_for_existing_post(api_client, valid_post_id):
    response = api_client.get_comments(valid_post_id)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

@pytest.mark.parametrize("post_id", [0, 999, 10**6])
def test_boundary_post_ids(api_client, post_id):
    response = api_client.get_comments(post_id)
    assert response.status_code in [200, 404]