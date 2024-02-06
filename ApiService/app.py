from flask import Flask
from extensions import db
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.user import UserResource
from resources.auth import AuthResource
from resources.search import SearchResource

def create_app() :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_emp.db'
    app.config['JWT_SECRET_KEY'] = 'my-key-qwer4321'
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
    api.add_resource(UserResource, '/api/user' , '/api/user/<string:user_email>')
    api.add_resource(AuthResource , '/api/login' , '/api/login/<string:user_email>')
    api.add_resource(SearchResource , '/api/employees' )

if __name__ == "__main__" :

    app = create_app()
    app.run(debug=True , port = 4000)