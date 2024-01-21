from extensions import db

class Employee(db.Model):
    first_name = db.Column(db.String(25), index=True)
    last_name = db.Column(db.String(25), index=True)
    email = db.Column(db.String(80), primary_key=True, index=True)
    phone_number = db.Column(db.String(13), index=True)
    dob = db.Column(db.Date)
    address = db.Column(db.String(100))
    # role = db.Column(db.String, default="employee")
    def __repr__(self) -> str:
        return '<Employee %r>' % self.email