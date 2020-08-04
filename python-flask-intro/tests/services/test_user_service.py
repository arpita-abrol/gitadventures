import logging
import pytest

from server.services import user_service

LOG = logging.getLogger(__name__)


@pytest.fixture
def user_list():
    return user_service.UserService()


def test_put_user(user_list):
    user_list.put_user({'name': 'Brian Doe'})


def test_get_user_by_id(user_list):
    user = user_list.put_user({'name': 'Jane Smith'})
    user = user_list.get_user_by_id(user['id'])

    LOG.debug('Received User: ' + str(user))


def test_get_user_by_unknown_id(user_list):
    user_list.put_user({'name': 'Bob Smith'})

    with pytest.raises(ValueError):
        user_list.get_user_by_id(23)


def test_get_first_10(user_list):
    for i in range(20):
        user_list.put_user({'name': 'Bob Smith' + str(i)})
        user_list.put_user({'name': 'Jane Smith' + str(i)})
        user_list.put_user({'name': 'Brian Doe' + str(i)})

    users = user_list.get_users(limit=10)

    LOG.debug('Received Users: ' + str(users))
    assert len(users) == 10


def test_remove_user_by_id(user_list):
    user_list.put_user({'name': 'Bob Smith'})

    user = user_list.remove_user_by_id(0)


def test_remove_user_by_unknown_id(user_list):
    user_list.put_user({'name': 'Bob Smith'})

    with pytest.raises(ValueError):
        user = user_list.remove_user_by_id(4)
