import os

from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

authorizations = {
	'Ride My Way': {
	'type': 'apiKey',
	'in': 'header',
	'name': 'X-API-KEY'
	}
}
app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,version=2.0,title='Ride My Way',authorizations=authorizations)


from .user_views import *
from .ride_views import *

api.add_resource(Signup,'/auth/signup')
api.add_resource(Signin,'/auth/login')
api.add_resource(PostRide,'/user/rides')

