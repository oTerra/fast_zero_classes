from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_must_return_ok_and_hello_world():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_html_must_return_html_with_hello_world():
    client = TestClient(app)
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Olá mundo!</h1>'
