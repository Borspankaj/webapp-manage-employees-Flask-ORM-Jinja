from models.employee import Employee
from extensions import db
from dto.employeeDto import EmployeeDto as emp_dto
class EmployeeService :

    def create_employee(args) :
        
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
        return emp_dto.get_employee_data(new_employee)
    
    def get_employee(employee_email) :
        employee = Employee.query.filter_by(employee_email).first()
        if employee:
            emp_dto.get_employee_data(employee)
        else:
            return None
        
    def update_employee(args , employee ) :

        employee.first_name = args['first_name']
        employee.last_name = args['last_name']
        employee.email = args['email']
        employee.phone_number = args['phone_number']
        employee.dob = args['dob']
        employee.address = args['address']

        db.session.commit()
        return emp_dto.get_employee_data(employee)

        


