from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from extensions import db
from services.auth import AuthService

class AuthResource(Resource) :

    def get(self , user_email) :
        try :
            if AuthService.delete_token(user_email) :
                return {' message ' : ' logout successfull'} , 200
            else :
                return {' error ' : 'unsuccessfull '} , 404
        except Exception as e:
            print(e)
            return {' error ' : 'unsuccessfull '} , 404
        
    
    def post(self):
        request_data = reqparse.request.get_json()
        try :
            user = AuthService.authenticate(request_data) 
            if user != None:
                access_token = AuthService.create_token(request_data['email'])
                print(access_token)
                # access_token = create_access_token(identity= request_data['email'] , additional_claims= {'role' : user['role']})
                response_data = {
                    'message' : 'login succesfull' ,
                    'user' : user
                }
                response = make_response(response_data)
                response.headers['Authorization'] = access_token
                response.status = 200
                return response
            else :
                
                response_data = {
                    'message' : 'Incorrect email/password'
                }
                response = make_response(response_data)
                response.status = 201
                return response
        except Exception as e :
            print(e)
            return { 'message' : 'error occured'}