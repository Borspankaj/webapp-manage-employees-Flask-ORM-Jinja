from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserToken(db.Model) :
    email = db.Column(db.String(80), primary_key = True, index = True)
    token = db.Column(db.String(128) , index = True)