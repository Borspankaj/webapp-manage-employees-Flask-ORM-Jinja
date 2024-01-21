from extensions import db

class Admin(db.Model) :
    email = db.Column(db.String(80) , primary_key =True)
    password = db.Column(db.String(25) , unique = True , nullable = False)
    def __repr__(self) -> str:
        return '<Admin %r>' % self.email