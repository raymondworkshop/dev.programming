# database - store data

from ml_service import db

class Entry(db.Model):
    __tablename = 'entries'
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.REAL, index=True)
    species = db.Column(db.String, index=True)
    score = db.Column(db.REAL)

    def __init__(self, age, species, score):
    	self.age = age
    	self.species = species
    	self.score = score

    def __repr__(self):
        return '%s' % (repr(self.age) + "@" + self.species + "@" + repr(self.score))
