#Important imports
from Coronaweb import db

#Creation of the database table in the form of a class and it's data members
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact = db.Column(db.String(12), nullable=False, unique=True)
    address = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    beds = db.Column(db.Integer, default=0)
    icubed = db.Column(db.Integer, default=0)
    oxygen = db.Column(db.Integer, default=0)
    vaccine = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"\nHospital(''{self.name}', \n'{self.email}', \n'{self.contact}, \n '{self.address}', \n '{self.password})\n"