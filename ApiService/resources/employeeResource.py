from flask_restful import Resource, reqparse
from extensions import db
from flask_jwt_extended import jwt_required , get_jwt_identity
from models.employee import Employee

class EmployeeResource(Resource) :
    @jwt_required()
    def get(self, employee_email):
        current_user = get_jwt_identity()

        # Fetch the employee from the database
        employee = Employee.query.filter_by(employee_email).first()

        if employee:
            return {
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'phone_number': employee.phone_number,
                'dob': employee.dob,
                'address': employee.address
            }
        else:
            return {'message': 'Employee not found'}, 404

    @jwt_required
    def post() :

        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
        parser.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('phone_number', type=str, required=True, help='Phone number cannot be blank')
        parser.add_argument('dob', type=str, required=True, help='Date of birth cannot be blank')
        parser.add_argument('address', type=str, required=True, help='Address cannot be blank')
        args = parser.parse_args()

        new_employee = Employee(
            first_name=args['first_name'],
            last_name=args['last_name'],
            email=args['email'],
            phone_number=args['phone_number'],
            dob=args['dob'],
            address=args['address'],
            
        )

        db.session.add(new_employee)
        db.session.commit()

        return {'message': 'Employee created successfully'}, 201
    
    @jwt_required()
    def put(self, employee_email):
        current_user = get_jwt_identity()

        # Fetch the employee from the database
        employee = Employee.query.filter_by(employee_email).first()

        if not employee:
            return {'message': 'Employee not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
        parser.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('phone_number', type=str, required=True, help='Phone number cannot be blank')
        parser.add_argument('dob', type=str, required=True, help='Date of birth cannot be blank')
        parser.add_argument('address', type=str, required=True, help='Address cannot be blank')
        args = parser.parse_args()

        # Update the employee details
        employee.first_name = args['first_name']
        employee.last_name = args['last_name']
        employee.email = args['email']
        employee.phone_number = args['phone_number']
        employee.dob = args['dob']
        employee.address = args['address']

        db.session.commit()

        return {'message': 'Employee updated successfully'}

    @jwt_required()
    def delete(self, employee_email):
        current_user = get_jwt_identity()

        # Fetch the employee from the database
        employee = Employee.query.filter_by(employee_email).first()

        if employee:
            db.session.delete(employee)
            db.session.commit()
            return {'message': 'Employee deleted successfully'}
        else:
            return {'message': 'Employee not found'}, 404






