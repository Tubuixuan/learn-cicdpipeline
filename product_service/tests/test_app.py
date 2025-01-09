import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_product(client):
    new_product = {"id": 103, "name": "Tablet"}
    response = client.post('/products', json=new_product)
    assert response.status_code == 201
    assert response.get_json()["product"]["id"] == 103