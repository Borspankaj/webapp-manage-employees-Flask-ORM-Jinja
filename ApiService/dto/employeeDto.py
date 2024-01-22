class EmployeeDto :
    def get_employee_data(employee) :
        return {
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'phone_number': employee.phone_number,
                'dob': employee.dob,
                'address': employee.address
            }