# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    """Fixture do testowania aplikacji Flask."""
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Testujemy główną stronę aplikacji."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the homepage' in response.data  # Przykładowy tekst na stronie

def test_contact_form(client):
    """Testujemy formularz kontaktowy."""
    response = client.post('/contact', data={'name': 'John', 'message': 'Hello'})
    assert response.status_code == 200
    assert b'Thank you for your message!' in response.data  # Oczekiwany tekst na stronie po wysłaniu formularza

def test_not_found(client):
    """Testujemy stronę 404 dla nieistniejącego endpointa."""
    response = client.get('/nonexistent')
    assert response.status_code == 404