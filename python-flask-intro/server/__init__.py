import os
from flask import Blueprint, Flask, abort, session, request, redirect, g
from flask_wtf.csrf import CSRFProtect
from flask_restx import Resource, Api, fields
from flask.json import jsonify

from server.services import user_service

app = Flask(__name__, template_folder="../public",
            static_folder="../public", static_url_path='')

app.config['ERROR_404_HELP'] = False
# csrf = CSRFProtect(app)

blueprint = Blueprint('api', __name__, url_prefix='/v1')
api = Api(blueprint,
          title="My API",
          version='v0.1',
          description='Description'
          )
app.register_blueprint(blueprint)

from server.routes import *  # noqa

if('FLASK_LIVE_RELOAD' in os.environ and
   os.environ['FLASK_LIVE_RELOAD'] == 'true'):
    import livereload
    app.debug = True
    server = livereload.Server(app.wsgi_app)
    server.serve(port=os.environ['port'], host=os.environ['host'])
