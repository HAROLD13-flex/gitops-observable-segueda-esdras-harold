from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_home_contains_student_name():
    client = app.test_client()
    response = client.get("/")
    assert b"Segueda" in response.data or b"Harold" in response.data
