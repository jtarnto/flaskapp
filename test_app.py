from app import app

def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_show_date():
    client = app.test_client()
    response = client.get('/date')
    assert b'Current date and time:' in response.data
