from flask import Flask
from extensions import db
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.employeeResource import EmployeeResource
from resources.loginResource import Login

def create_app() :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////emp.db'
    register_extensions(app)
    return app

def register_extensions(app) :
    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)
    register_api(api)
    with app.app_context():
        db.create_all()

def register_api(api) :
    api.add_resource(EmployeeResource, '/api/employee' , '/api/employee/<string:employee_email>')
    api.add_resource(Login , '/api/login')

if __name__ == "__main__" :

    app = create_app()
    app.run(debug=True)
