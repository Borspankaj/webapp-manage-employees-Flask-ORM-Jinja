from flask_restful import Resource, reqparse
from services.user import UserService
from services.auth import AuthService
class SearchResource(Resource) :
    
    def get(self) :
        token  = reqparse.request.headers.get('Authorization')
        print(token)
        if AuthService.is_authorized(token) :
            response_data = UserService.get_employees()
            return response_data
        else :
            return {'message': 'Unauthorized access'}, 403
    
    def post(self) :
        token  = reqparse.request.headers.get('Authorization')
        if AuthService.is_authorized(token) :
            request_data = reqparse.request.get_json()
            response_data = UserService.search_employees(request_data['keyword'])
            return response_data
        else :
            return {'message': 'Unauthorized access'}, 403