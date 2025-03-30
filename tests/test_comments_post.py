import pytest

def test_create_comment(api_client, valid_post_id, valid_comment_data):
    response = api_client.create_comment(valid_post_id, valid_comment_data)
    assert response.status_code == 201
    assert "id" in response.json()

def test_comment_structure(api_client, valid_post_id):
    response = api_client.get_comments(valid_post_id)
    comment = response.json()[0]
    assert all(key in comment for key in ["id", "postId", "name", "email", "body"])