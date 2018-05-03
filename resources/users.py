from flask import Blueprint, jsonify
from flask_restplus import Resource, Api
from models import model

user = model.Users()


class Users(Resource):
    def get(self):
        return jsonify(user.get_users())


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)

api.add_resource(Users,
                 '/users',
                 endpoint='users')
