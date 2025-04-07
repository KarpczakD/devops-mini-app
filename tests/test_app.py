import sys
import os
import pytest

# Dodaj ścieżkę do katalogu, w którym znajduje się app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importujemy aplikację

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
    assert b'Thank you for your message, John!' in response.data  # Uwzględniamy imię w odpowiedzi

def test_not_found(client):
    """Testujemy stronę 404 dla nieistniejącego endpointa.""" 
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_about_page(client):
    """Testujemy stronę o aplikacji."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'DevOps demo app' in response.data

def test_login_success(client):
    """Testujemy poprawne logowanie."""
    response = client.post('/login', data={'username': 'admin', 'password': 'password'})
    assert response.status_code == 302  # Status 302 oznacza przekierowanie po udanym logowaniu
    assert response.location == '/'  # Oczekujemy tylko ścieżki, nie pełnego URL

def test_login_failure(client):
    """Testujemy niepoprawne logowanie."""
    response = client.post('/login', data={'username': 'wronguser', 'password': 'wrongpass'})
    assert response.status_code == 200  # Powinno pozostać na stronie logowania
    assert b'Invalid credentials. Please try again.' in response.data  # Oczekiwany komunikat błędu

def test_change_password_success(client):
    """Testujemy udaną zmianę hasła."""
    response = client.post('/change-password', data={
        'new_password': 'newpassword123',
        'confirm_password': 'newpassword123'
    })
    assert response.status_code == 302  # Przekierowanie po udanej zmianie hasła
    assert response.location == 'http://localhost/'  # Sprawdź, czy przekierowanie prowadzi na stronę główną

    # Teraz sprawdzimy, czy komunikat o sukcesie pojawi się na stronie głównej
    response = client.get('/')
    assert b'Password changed successfully!' in response.data  # Oczekiwany komunikat sukcesu

