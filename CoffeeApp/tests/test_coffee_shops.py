def test_get_coffee_shop(client):
    response = client.get("/coffee_shops")
    assert response.status_code == 200
    assert response.json() == []


def test_create_coffee_shop(client):
    payload = {"name": "example name"}
    response = client.post("/coffee_shops/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "example name"
