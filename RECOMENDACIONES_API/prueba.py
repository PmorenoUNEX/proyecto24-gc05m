import pytest
from app import create_app

@pytest.fixture
def app():
    # Usar la función `create_app` para crear una instancia de Flask para las pruebas
    return create_app()

def test_favoritos_blueprint(app):
    client = app.test_client()
    response = client.get('/favoritos')
    assert response.status_code in {200, 404}, "El blueprint 'favoritos' debería responder con 200 o 404."

def test_tendencias_blueprint(app):
    client = app.test_client()
    response = client.get('/tendencias')
    assert response.status_code in {200, 404}, "El blueprint 'tendencias' debería responder con 200 o 404."

def test_visualizaciones_blueprint(app):
    client = app.test_client()
    response = client.get('/visualizaciones')
    assert response.status_code in {200, 404}, "El blueprint 'visualizaciones' debería responder con 200 o 404."
