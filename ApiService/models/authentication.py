from extensions import db

class Auth(db.Model) :
    email = db.Column(db.String(80) , primary_key =True)
    role = db.Column(db.String(10))
    password = db.Column(db.String(25) , unique = True , nullable = False)
    def __repr__(self) -> str:
        return '<Auth %r>' % self.email