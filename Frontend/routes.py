from flask import Blueprint , render_template , request, redirect, url_for
from forms.LoginForm import LoginForm
from services.auth import AuthService

mod = Blueprint('routes' , __name__)

@mod.route("/") 
def home() :
    return "running"

@mod.route("/login-page")
def login_page() :
    form = LoginForm()  
    return render_template('login.html' , form = form )

@mod.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        # Process the form data here
        email = request.form['email']
        password = request.form['password']

        # Call the authentication service
        if AuthService.authenticate(email, password):
            # Redirect to a success page or perform additional actions
            return redirect(url_for('success'))
        else:
            # Authentication failed, you may want to redirect to a login page with an error message
            return redirect(url_for('login_page'))

    # For simplicity, return a response for now
    return "Invalid request method"

