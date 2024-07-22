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


def test_duplicate_email_returns_409(client):
    payload = {"email": "user@example.com", "name": "example user"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    error_response = client.post("/users", json=payload)
    assert error_response.status_code == 409


def test_missing_email_returns_422(client):
    payload = {"name": "example user"}
    response = client.post("/users", json=payload)
    assert response.status_code == 422


def test_empty_email_input(client):
    payload = {"email": "", "name": "example user"}
    response = client.post("/users", json=payload)
    assert response.status_code == 422


def test_empty_name_input(client):
    payload = {"email": "user@example.com", "name": ""}
    response = client.post("/users", json=payload)
    assert response.status_code == 422
