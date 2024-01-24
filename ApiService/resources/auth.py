from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from extensions import db
from services.auth import AuthService as auth_

class AuthResource(Resource) :

    def post(self):
        request_data = reqparse.request.get_json()
        try :
            if auth_.authenticate(request_data) :
                access_token = create_access_token(identity= request_data['email'])
                response_data = {
                    'message' : 'login succesfull'
                }
                response = make_response(response_data)
                response.headers['Authorization'] = f'Bearer {access_token}'
                return response
            else :
                return { 'message' : 'incorrect email/password'}
        except Exception as e :
            print(e)
            return { 'message' : 'error occured'}

