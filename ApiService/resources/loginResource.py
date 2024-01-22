from flask_restful import Resource, reqparse
from extensions import db
from models.authentication import Auth
from flask_jwt_extended import create_access_token


class Login(Resource) :

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        args = parser.parse_args()
        email=args['email']
        user = Auth.query.filter_by(email = email).first()
        if user and args['password'] == user.password :
            access_token = create_access_token(identity=email)
            return {'message': 'Login successful' , 
                    'access_token' : access_token }, 200
        else:
            return {'message': 'Invalid email or password'}, 401