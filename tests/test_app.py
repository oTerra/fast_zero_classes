from http import HTTPStatus


def test_read_root_must_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_username',
            'email': 'test@email.com',
            'password': 'test_password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test_username',
        'email': 'test@email.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'test_username', 'email': 'test@email.com'}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'updated_test_username',
            'email': 'test@email.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'updated_test_username',
        'email': 'test@email.com',
    }


def test_update_user_exception_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'id': 2,
            'username': 'updated_test_username',
            'email': 'test@email.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'id': 1,
            'username': 'updated_test_username',
            'email': 'test@email.com'
        }


def test_read_user_exception_user_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_exception_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
