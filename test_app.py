from app import app

def test_joke_route():
    client = app.test_client()
    response = client.get("/joke")
    assert response.status_code == 200
    assert "joke" in response.get_json()
