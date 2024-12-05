from app import app


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Welcome to the Postgres Dockerized App!"


def test_add_record(client):
    response = client.post('/add', json={"name": "TestUser", "age": 30})
    assert response.status_code == 201
    assert "id" in response.json
