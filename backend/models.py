from app import db

fragrance_notes =  db.Table('fragrance_notes',
    db.Column('fragrance_id', db.Integer, db.ForeignKey('fragrance.id'), primary_key=True),
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'), primary_key=True)
    db.Column('position', db.String(10)) #top, heart, base
)

fragrance_tyoes = db.Table('fragrance_types',
    db.Column('fragrance_id', db.Integer, db.ForeignKey('fragrance.id'), primary_key=True),
    db.Column('type_id', db.Integer, db.ForeignKey('fragrance_type.id'), primary_key=True)
)

class Fragrance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=True) #men, women, unisex
    concentration = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    
    notes = db.relationship('Note', secondary=fragrance_notes, 
                          backref=db.backref('fragrances', lazy='dynamic'))
    types = db.relationship('FragranceType', secondary=fragrance_types, 
                          backref=db.backref('fragrances', lazy='dynamic'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'release_year': self.release_year,
            'gender': self.gender,
            'concentration': self.concentration,
            'description': self.description,
            'image_url': self.image_url
            'notes': [{'id': note.id, 'name': note.name, 'category': note.category} for note in self.notes],
            'types': [{'id': type.id, 'name': type.name} for type in self.types]
        }

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50)), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }
        
class FragranceType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }