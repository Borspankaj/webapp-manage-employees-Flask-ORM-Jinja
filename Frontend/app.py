from flask import Flask
from routes import mod
from admin_routes import admin
from flask_session import Session
from flask_jwt_extended import JWTManager

def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'emp-123-ewq'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config['JWT_SECRET_KEY'] = 'my-key-qwer4321'
    JWTManager(app)
    Session(app)
    app.register_blueprint(mod, url_prefix='/')
    app.register_blueprint(admin , url_prefix = '/admin')
    return app

if __name__ == "__main__" :
    app = create_app()
    app.run(debug=True , port = 5000)