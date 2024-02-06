from flask import session , flash
import requests

class UserService :
    @staticmethod   
    def get_users() : 
        api_url = 'http://127.0.0.1:4000/api/employees' 
        headers = {'Authorization':session['token']}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            employee_list = response.json()
            return employee_list
        return None
            
    @staticmethod
    def get_employee_details(emp_email):
        api_url = 'http://127.0.0.1:4000/api/user/' + emp_email
        headers = {'Authorization':session['token']}
        response = requests.get(api_url , headers= headers)
        if response.status_code == 200 : 
            employee_details = response.json()
            return employee_details
        return None
    
    @staticmethod
    def search_employees(search_parameter) :
        api_url = 'http://127.0.0.1:4000/api/employees'
        headers = {'Authorization':session['token']}
        payload = {'keyword' :search_parameter}
        response = requests.post(api_url , json= payload , headers= headers)
        
        if response.status_code == 200 :
            emp_list = response.json()
            return emp_list
        return None
        
        
    @staticmethod
    def create_user(form):
        api_url = 'http://127.0.0.1:4000/api/user'
        # headers = {'Authorization': session['token']}
        print("----")
        payload = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'phone_number': form.phone_number.data,
            'password' : form.password.data ,
            'role': form.role.data if form.role.data != None else 'EMP',
            'address': form.address.data
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return True
        else:
            return False
        
    @staticmethod
    def update_user(emp_email, form):
        api_url = f'http://127.0.0.1:4000/api/user/{emp_email}'
        headers = {'Authorization': session['token']}
        payload = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'phone_number': form.phone_number.data,
            'role': form.role.data,
            'address': form.address.data
        }
        
        response = requests.put(api_url, json=payload, headers=headers)

        print(response.status_code)
        if response.status_code == 200:
            flash('User updated successfully!', 'success')
            return True
        else:
            flash('Failed to update user. Please try again.', 'danger')
            return False

    @staticmethod
    def delete_user(emp_email):
        api_url = f'http://127.0.0.1:4000/api/user/{emp_email}'
        headers = {'Authorization': session['token']}
        
        response = requests.delete(api_url, headers=headers)

        if response.status_code == 200:
            flash('User deleted successfully!', 'success')
            return True
        else:
            flash('Failed to delete user. Please try again.', 'danger')
            return False