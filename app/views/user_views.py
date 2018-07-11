from flask import request
from flask_restplus import Resource, fields

from ..model.signup import Register
from .views import api

signup_model = api.model('signup',{
	'first_name': fields.String,
	'last_name': fields.String,
	'email': fields.String,
	'user_type': fields.String,
	'password': fields.String
	}) 


class Signup(Resource):
	"""
	class for user signup method
	"""
	@api.expect(signup_model)
	def post(self):
		data = request.get_json()
		register = Register(data)
		if register.verify_data() is not False:
			return register.verify_data()
		else:
			return {'result':'test'}