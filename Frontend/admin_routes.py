from flask import Blueprint , render_template , request, redirect, url_for , session
from forms.UserForm import UserForm
from services.UserService import UserService
import utils
admin = Blueprint('admin' , __name__)

@admin.route('/add_employee', methods=['GET' , 'POST'])
def add_employee():
    form = UserForm()
    if form.validate_on_submit():
        try :
            if UserService.create_user(form) :
                return redirect(url_for('routes.homepage'))
            else :
                return render_template('add_employee.html', form=form , error_message = "Error Occured")
        except Exception as e:
            print(e)
            return render_template('add_employee.html', form=form , error_message = "Error Occured")
    return render_template('add_employee.html', form=form)

@admin.route('/update_employee/<string:emp_email>', methods=['GET' , 'POST'])
def update_employee(emp_email):
    employee_details = UserService.get_employee_details(emp_email)
    form = utils.get_edit_form(employee_details)
    if form.validate_on_submit():
        try :
            if UserService.update_user(emp_email ,form) :
                return redirect(url_for('routes.home_page'))
            else :
                return render_template('update_employee.html', form=form , error_message = "Error Occured")
        except Exception as e:
            print(e)
            return render_template('update_employee.html', form=form , error_message = "Error Occured")
    
    return render_template('update_employee.html', form=form)


@admin.route('/delete_employee/<string:emp_email>', methods=['POST'])
def delete_employee(emp_email):
    try :
        if UserService.delete_user(emp_email) :
            return redirect(url_for('routes.home_page'))
        else :
            return redirect(url_for('routes.home_page'))
    except Exception as e:
        print(e)
        return redirect(url_for('routes.home_page'))
    