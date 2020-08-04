
from flask import jsonify
from flask_restx import Namespace, Resource
from server import app, api
from server.routes import prometheus

health_namespace = Namespace('health', description='Return Application Health')

api.add_namespace(health_namespace)


@health_namespace.route("")
class Health(Resource):
    @prometheus.track_requests
    def get(self):
        state = {"status": "UP"}
        return jsonify(state)
