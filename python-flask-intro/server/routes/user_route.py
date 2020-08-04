import logging

from flask import jsonify, request, Response, g
from flask_restx import abort, Namespace, Resource, fields
from server import app, api
from server.routes import prometheus

from server.services import user_service

LOG = logging.getLogger(__name__)

# Only doing this as we're not using a database
# this is NOT recommended
user_data = user_service.UserService()

user_namespace = Namespace('user',
                           description='Interface for User Resource')

api.add_namespace(user_namespace)

user_fields = api.model('User',
                        {
                            'name': fields.String
                        })


@user_namespace.route("")
class User(Resource):

    @prometheus.track_requests
    @api.param('id', description='user id', type='integer')
    def get(self):
        if not request.args.get('id'):
            response = user_data.get_users()
        else:
            try:
                response = user_data.get_user_by_id(
                                        int(request.args.get('id')))
            except ValueError as ex:
                abort(404, message=str(ex))

        return jsonify(response)

    @prometheus.track_requests
    @api.expect(user_fields)
    def post(self):
        LOG.debug('Create new User: ' + str(api.payload))
        try:
            user = user_data.put_user(api.payload)
        except ValueError as e:
            return {'success': False, 'message': str(e)}, 400

        return user, 201

    @prometheus.track_requests
    @api.param('id', description='user id', type='integer', required=True)
    def delete(self):
        LOG.debug('Delete User: ' + request.args.get('id'))
        try:
            user_data.remove_user_by_id(int(request.args.get('id')))
        except ValueError as e:
            return {'success': False, 'message': str(e)}, 400

        return jsonify({'success': True})
