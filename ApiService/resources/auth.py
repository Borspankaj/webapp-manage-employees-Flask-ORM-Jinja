from flask_restful import Resource, reqparse
from extensions import db
from flask_jwt_extended import create_access_token
from services.auth import AuthService as auth_
class AuthResource(Resource) :

    def post(self):
        request_data = reqparse.request.get_json()
        try :
            if auth_.authenticate(request_data) :
                access_token = create_access_token(identity= request_data['email'])
                return { 'access_token' : access_token ,
                        'message' : 'login succesfull'} 
            else :
                return { 'message' : 'incorrect email/password'}
        except Exception as e :
            return { 'message' : 'error occured'}
    



        