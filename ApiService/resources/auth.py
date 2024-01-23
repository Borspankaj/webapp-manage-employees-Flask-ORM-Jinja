from flask_restful import Resource, reqparse
from extensions import db
from flask_jwt_extended import create_access_token

class AuthResource(Resource) :

    def post(self):
        pass