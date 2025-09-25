from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Qoutes" in response.data

def test_get_all_qoutes():
    client = app.test_client()
    response = client.get("/jokes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_qoute():
    client = app.test_client()
    response = client.post("/jokes", json={"text": "Testing qoute"})
    assert response.status_code == 201
    assert "id" in response.get_json()
    assert "text" in response.get_json()

def test_update_qoute():
    client = app.test_client()
    response = client.put("/jokes/1", json={"text": "Updated qoute"})
    assert response.status_code == 200
    assert response.get_json()["text"] == "Updated qoute"

def test_delete_qoute():
    client = app.test_client()
    response = client.delete("/jokes/2")
    assert response.status_code == 200
    assert "deleted" in response.get_json()["message"]
def test_get_qoute_by_id():
    client = app.test_client()
    response = client.get("/jokes/1")
    assert response.status_code == 200
    assert "id" in response.get_json() and "text" in response.get_json()