import enum
from src.main import db

class AnimalSex(enum.Enum):
    FEMALE = 'f'
    MALE = 'm'

class AnimalTypes(enum.Enum):
    HEN = 'hen'
    DOG = 'dog'
    CATTLE = 'cattle'
    PIG = 'pig'
    HORSE = 'horse'


class Animals(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex = db.Column(db.Enum(AnimalSex), nullable=False)
    wheight = db.Column(db.Float)
    specie = db.Column(db.String)
    animal_type = db.Column(db.Enum(AnimalTypes), nullable=False)

    def __repr__(self):
        return (""
            + f"<Animal {self.name}:"
            + f" [animal_type: {self.animal_type}"
            + f", sex: {self.sex}"
            + f", specie: {self.specie}]>"
        )
