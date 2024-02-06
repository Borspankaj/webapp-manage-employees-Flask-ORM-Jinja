from flask import Blueprint , render_template , request, redirect, url_for , session
from forms.LoginForm import LoginForm
from forms.UserForm import UserForm
from services.AuthService import AuthService
from services.AccountService import AccountService
from services.UserService import UserService
from flask_jwt_extended import jwt_required , get_jwt_identity 

mod = Blueprint('routes' , __name__)

@mod.route("/") 
def home() :
    return redirect(url_for('routes.register'))

@mod.route("/register" , methods=['GET' ,'POST']) 
def register() :
    form = UserForm()
    if form.validate_on_submit():
        print("---")
        print(form)
        try :
            print('1111')
            if UserService.create_user(form) :
                print(222)
                return redirect(url_for('routes.login_page'))
            else :
                print(333)
                render_template('register_employee.html', form=form , error_message = "Error Creating User")
        except Exception as e:
            print(444)
            print(e)
            render_template('register_employee.html', form=form , error_message = "Error Creating User")
    return render_template('register_employee.html', form=form)
    
@mod.route("/login-page" , methods = ['GET' , 'POST'])
def login_page() :
    form = LoginForm() 
    if form.validate_on_submit() :
        email = form.email.data
        password = form.password.data
        if AuthService.authenticate(email, password) :
            return redirect(url_for('routes.home_page'))
        else:
            return render_template('login.html' , form = form , error_message = "Incorect password")
        
    return render_template('login.html' , form = form )



@mod.route("/home-page") 
def home_page() :
    is_admin = True if session['role'] == 'ADMIN' else False
    emp_list = UserService.get_users()
    return render_template('homepage.html' , emp_list = emp_list , is_admin = is_admin)
    
    
@mod.route('/employee_details/<string:emp_email>', methods=['GET'])
def employee_details(emp_email):
    is_admin = True if session['role'] == 'ADMIN' else False
    employee_details = UserService.get_employee_details(emp_email)
    return render_template('employee_details.html', employee_details=employee_details , is_admin = is_admin)
    
@mod.route('/search_employees', methods=['GET'])
def search_employees():
    is_admin = True if session['role'] == 'ADMIN' else False
    search_parameter = request.args.get('keyword', '')
    emp_list = UserService.search_employees(search_parameter)
    return render_template('homepage.html' , emp_list = emp_list , is_admin = is_admin)
    
@mod.route('/logout') 
def logout() :
    if AccountService.logout() :
        return redirect(url_for('routes.login_page'))
    else :
        return redirect(url_for('routes.home_page') )