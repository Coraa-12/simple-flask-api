# tests/test_app.py
import pytest
from app import app as flask_app # Import your Flask app object

@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    # You could add test-specific configurations here if needed
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture()
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture()
def runner(app):
    """A test runner for the app's Click commands."""
    # Not needed for basic endpoint testing, but often included
    return app.test_cli_runner()

# --- Your Actual Tests ---

def test_home_route(client):
    """Test the '/' route."""
    response = client.get('/')
    # Check the status code is 200 OK
    assert response.status_code == 200
    # Check if the JSON response is what we expect
    expected_json = {"message": "Hello from my Flask App in WSL!"}
    assert response.json == expected_json

def test_ping_route(client):
    """Test the '/ping' route."""
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {"response": "pong"}