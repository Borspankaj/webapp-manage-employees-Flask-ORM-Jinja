from extensions import db

class Admin(db.Model) :
    email = db.Column(db.String(80) , primary_key =True)
    def __repr__(self) -> str:
        return '<Admin %r>' % self.email