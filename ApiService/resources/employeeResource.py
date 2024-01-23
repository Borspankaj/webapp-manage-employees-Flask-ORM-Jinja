from flask_restful import Resource, reqparse
from extensions import db
from flask_jwt_extended import jwt_required , get_jwt_identity
from models.employee import Employee
from services.employeeService import EmployeeService as es
from utils import utils as ut

class EmployeeResource(Resource) :
    # @jwt_required()
    def get(self, employee_email):
        current_user = get_jwt_identity()
        employee_details = es.get_employee(employee_email)
        if employee_details : return employee_details
        else: return {'message': 'Employee not found'}, 404

    # @jwt_required
    def post(self) :
        # current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        args = ut.get_args(parser)
        response_data = es.create_employee(args)
        return {'message': 'Employee created successfully' ,
                'employee' : response_data}, 200
    
    # @jwt_required()
    def put(self, employee_email):

        parser = reqparse.RequestParser()
        args = ut.get_args(parser)
        response_data = es.update_employee(args , employee_email)
        if response_data != None:
            return {'message': 'Employee updated successfully' ,
                'data' : response_data } , 200
        else :
            return {'message': 'Employee not found'}, 404

    # @jwt_required()
    def delete(self, employee_email):
        current_user = get_jwt_identity()
        response_data = es.delete_employee(employee_email)
        if response_data != None :
            return {'message': 'Employee deleted successfully'}
        else:
            return {'message': 'Employee not found'}, 404






