from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), index=True)
    last_name = db.Column(db.String(25), index=True)
    email = db.Column(db.String(80), unique=True, index=True)
    phone_number = db.Column(db.String(13), index=True)
    # dob = db.Column(db.Date)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(100))
    role = db.Column(db.String)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self) -> str:
        return f'<User {self.id}>'