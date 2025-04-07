import sys
import os
import pytest

# Dodaj ścieżkę do katalogu, w którym znajduje się app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importuj aplikację

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

def test_about_page(client):
    """Testujemy stronę o aplikacji."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'DevOps demo app' in response.data