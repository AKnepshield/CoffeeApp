def test_get_user(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user(client):
    payload = {"email": "user@example.com", "name": "example user"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"
    assert response.json()["name"] == "example user"
    assert response.json()["id"] is not None
