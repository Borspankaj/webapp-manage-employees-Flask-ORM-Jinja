from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required , get_jwt_identity
from services.user import UserService as us
from services.auth import AuthService 

class UserResource(Resource) :
    
    def get(self, user_email):
        token  = reqparse.request.headers.get('Authorization')
        print(token)
        if AuthService.is_authorized(token) :
            
            response_data = us.get_user(user_email)
            if response_data : return response_data
            else: return {'message': 'Employee not found'}, 404
        else :
            return {'message': 'Unauthorized access'}, 403

    
    def post(self) :
        # token  = reqparse.request.headers.get('Authorization')
        # if AuthService.is_authorized(token) :
            request_data = reqparse.request.get_json()
            print(request_data)
            try :
                response_data = us.create_user(request_data)
            
                return {'message': 'Employee created successfully' ,
                        'data' : response_data}, 200
            except Exception as e:
                return {'message' : 'internal error' , 
                        'error' : e}
        # else :
        #     return {'message': 'Unauthorized access'}, 403
            
        
    
    def put(self, user_email):
        token  = reqparse.request.headers.get('Authorization')
        if AuthService.is_authorized_admin(token) :
            request_data = reqparse.request.get_json()
            response_data = us.update_user(request_data , user_email)
            if response_data != None:
                return {'message': 'Employee updated successfully' ,
                    'data' : response_data } , 200
            else :
                return {'message': 'Employee not found'}, 404
        else :
            return {'message': 'Unauthorized access'}, 403

    
    def delete(self, user_email):
        token  = reqparse.request.headers.get('Authorization')
        if AuthService.is_authorized_admin(token) :
       
            response_data = us.delete_user(user_email)
            if response_data != None :
                return {'message': 'Employee deleted successfully'}
            else:
                return {'message': 'Employee not found'}, 404
        else :
            return {'message': 'Unauthorized access'}, 403