from flask import Blueprint
from flask import render_template

mod = Blueprint('views' , __name__)

@mod.route("/login-page")
def login_page() :
    return render_template(
        'login.html' 
    )