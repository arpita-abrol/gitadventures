import logging

LOG = logging.getLogger(__name__)


class UserService:

    def __init__(self):
        LOG.info('Initialising Empty User list')
        self._users = []
        self._next_id = 0

    def put_user(self, user):
        if 'name' not in user:
            raise ValueError('Invalid User, Refusing to Put: [' + user + ']')

        user['id'] = self._next_id
        self._next_id += 1
        self._users.append(user)

        return user

    def get_users(self, limit=10, start_idx=0):
        LOG.debug('get all')

        return self._users[start_idx:limit]

    def get_user_by_attr(self, attr, attr_value):
        LOG.debug('get_user_by [' + str(attr) +
                  '] : [' + str(attr_value) + ']')

        for user in self._users:
            if user[attr] == attr_value:
                return user

        raise ValueError('User not found for [' + str(attr) +
                         '] : [' + str(attr_value) + ']')

    def get_user_by_id(self, id):
        return self.get_user_by_attr('id', id)

    def remove_user_by_id(self, id):
        for user in self._users:
            if user['id'] == id:
                return self._users.remove(user)

        raise ValueError('User not found for id : [' +
                         str(id) + ']')
