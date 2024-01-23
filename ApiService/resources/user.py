from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required , get_jwt_identity
from services.user import UserService as us

class UserResource(Resource) :
    # @jwt_required()
    def get(self, user_email):
        # current_user = get_jwt_identity()
        response_data = us.get_user(user_email)
        if response_data : return response_data
        else: return {'message': 'Employee not found'}, 404

    # @jwt_required
    def post(self) :
        # current_user = get_jwt_identity()
        request_data = reqparse.request.get_json()
        print(request_data)
        try :
            response_data = us.create_user(request_data)
            return {'message': 'Employee created successfully' ,
                    'data' : response_data}, 200
        except Exception as e:
            return {'message' : 'internal error' , 
                    'error' : e}
        
    # @jwt_required()
    def put(self, user_email):
        request_data = reqparse.request.get_json()
        response_data = us.update_user(request_data , user_email)
        if response_data != None:
            return {'message': 'Employee updated successfully' ,
                'data' : response_data } , 200
        else :
            return {'message': 'Employee not found'}, 404

    # @jwt_required()
    def delete(self, user_email):
        # current_user = get_jwt_identity()
        response_data = us.delete_user(user_email)
        if response_data != None :
            return {'message': 'Employee deleted successfully'}
        else:
            return {'message': 'Employee not found'}, 404






