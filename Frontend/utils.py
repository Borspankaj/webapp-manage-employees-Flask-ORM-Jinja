from forms.UserForm import UserForm
def get_edit_form(employee_details) :
    form = UserForm(
        first_name = employee_details['first_name'] ,
        last_name = employee_details['last_name'] ,
        phone_number = employee_details['phone_number'] ,
        email = employee_details['email'] ,
        address = employee_details['address'] ,
        role = employee_details['role']
        
    )

    return form
