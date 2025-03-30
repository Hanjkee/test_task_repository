def test_create_comment(api_client, valid_post_id):
    data = {
        "name": "Test User",
        "email": "test@example.com",
        "body": "Test content"
    }
    response = api_client.create_comment(valid_post_id, data)
    assert response.status_code == 201
    assert "id" in response.json()