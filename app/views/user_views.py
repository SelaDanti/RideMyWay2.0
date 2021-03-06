import jwt
import datetime

from flask import request
from flask_restplus import Resource, fields

from ..model.signup import Register
from ..model.signin import Login
from .views import api, app

signup_model = api.model('signup',{
	'first_name': fields.String,
	'last_name': fields.String,
	'email': fields.String,
	'user_type': fields.String,
	'password': fields.String
	}) 
signin_model = api.model('singin',{
	'email': fields.String,
	'password': fields.String
	})


class Signup(Resource):
	"""
	class for user signing up users
	"""
	@api.expect(signup_model)
	def post(self):
		data = request.get_json()
		register = Register(data)
		if register.verify_data() is not False:
			return register.verify_data()
		else:
			if register.email_exist() is not True:
				return register.insert_data()
			else:
				return {'result':'Email exist'},405


class Signin(Resource):
	"""
	class for signing in users
	"""
	@api.expect(signin_model)
	def post(self):
		data = request.get_json()
		login = Login(data)
		if login.verify_data() is not False:
			return login.verify_data()
		else:
			token = jwt.encode({'user':data['email'],
				'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=230)},
				app.config['SECRET_KEY'])
			token = token.decode('UTF-8')
			return login.login(token)