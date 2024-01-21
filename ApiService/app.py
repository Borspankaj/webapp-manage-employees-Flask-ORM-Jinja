from flask import Flask
from ApiService.extensions import db

def create_app() :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////emp.db'
    register_extensions(app)
    return app

def register_extensions(app) :
    db.init_app(app)
    with app.app_context():
        db.create_all()

if __name__ == "__main__" :
    app = create_app()
    app.run(debug=True)
