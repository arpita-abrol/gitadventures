
import json
import logging
import pytest
import urllib.parse

from server import app

LOG = logging.getLogger(__name__)


@pytest.fixture
def app_client():
    app_client = app.test_client()
    app_client.testing = True
    yield(app_client)


def test_root_endpoint(app_client):
    response = app_client.get('/')
    assert response.status_code == 200
    response.close()


def test_health_endpoint(app_client):
    path = '/v1/health'
    result = json.loads(app_client.get(path).data)
    LOG.debug(path + ' : ' + str(result))
    assert result['status'] == 'UP'


def test_put_user(app_client):
    path = '/v1/user'
    response = app_client.post(
                        path,
                        data=json.dumps({'name': 'Dave Roberts'}),
                        content_type='application/json')

    LOG.debug('POST response: ' + str(response))
    LOG.debug('POST response data: ' + str(response.data))
    assert response.status_code == 201

    return json.loads(response.data)


def test_get_all_users(app_client):
    test_put_user(app_client)
    path = '/v1/user'
    response = app_client.get(path)

    result_data = json.loads(response.data)
    LOG.debug(path + ' : ' + str(result_data))
    assert response.status_code == 200


def test_get_user(app_client):
    user = test_put_user(app_client)
    path = '/v1/user?id=' + str(user['id'])
    response = app_client.get(path)

    result_data = json.loads(response.data)
    LOG.debug(path + ' : ' + str(result_data))
    assert response.status_code == 200
    assert result_data['name'] == 'Dave Roberts'


def test_get_unkown_user(app_client):
    path = '/v1/user?id=345'
    response = app_client.get(path)

    result_data = json.loads(response.data)
    LOG.debug(path + ' : ' + str(result_data))
    assert response.status_code == 404
