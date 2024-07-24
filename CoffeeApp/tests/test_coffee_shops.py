def test_get_coffee_shop(client):
    response = client.get("/coffee_shops")
    assert response.status_code == 200
    assert response.json() == []
