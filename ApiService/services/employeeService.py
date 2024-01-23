from models.employee import Employee
from extensions import db
from dto.employeeDto import EmployeeDto as emp_dto
from datetime import datetime

class EmployeeService :

    def create_employee(args) :
        
        new_employee = Employee(
            first_name=args['first_name'],
            last_name=args['last_name'],
            email=args['email'],
            phone_number=args['phone_number'],
            dob=datetime.strptime(args['dob'], '%Y-%m-%d').date().isoformat(),
            address=args['address'],
            
        )

        db.session.add(new_employee)
        db.session.commit()
        return emp_dto.get_employee_data(new_employee)
    
    def get_employee(employee_email) :
        employee = Employee.query.filter_by(employee_email).first()
        if employee:
            emp_dto.get_employee_data(employee)
        else:
            return None
        
    def update_employee(args , employee_email ) :

        employee = Employee.query.filter_by(employee_email).first()
        if not employee:
            return None
        
        employee.first_name = args['first_name']
        employee.last_name = args['last_name']
        employee.email = args['email']
        employee.phone_number = args['phone_number']
        employee.dob = datetime.strptime(args['dob'], '%Y-%m-%d').date().isoformat()
        employee.address = args['address']

        db.session.commit()
        return emp_dto.get_employee_data(employee)
    
    def delete_employee(employee_email) :
        employee = Employee.query.filter_by(employee_email).first()
        if employee:
            employee_data = emp_dto.get_employee_data(employee)
            db.session.delete(employee)
            db.session.commit()
            return employee_data
        return None
            


        


