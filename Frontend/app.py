from flask import Flask
from routes import mod

def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'emp-123-ewq'
    app.register_blueprint(mod, url_prefix='/')
    return app

if __name__ == "__main__" :
    app = create_app()
    app.run(debug=True , port = 5000)