from typing import NamedTuple, Dict
from enum import Enum

class AnimalTypes(Enum):
    HEN = 'hen'
    DOG = 'dog'
    CATTLE = 'cattle'
    SUINE = 'suine'
    HORSE = 'horse'

class Animals(NamedTuple):

    animal_type: Enum(AnimalTypes)
    name: str
    specie: str
    weight: float
    specification: Dict[str, str]


# class Hen(NamedTuple):
#     name: str
#     eggs_per_week: int
#     specie: str

# class Dog(NamedTuple):
#     name: str
#     age: int
#     specie: str

# class Cattle(NamedTuple):
#     name: str
#     sex: str
#     wheight: float

# class Suine(NamedTuple):
#     name: str
#     age: int
#     wheight: float

# class Horse(NamedTuple):
#     name: str
#     age: int
#     racer: bool

# Hen = namedtuple("Hen", "name eggs_per_week specie")
# Dog = namedtuple("Dog", "name age specie")
# Cattle = namedtuple("Cattle", "name sex wheight")
# Suine = namedtuple("Suine", "name age wheight")
# Horse = namedtuple("Horse", "name age racer")

# animals = {
#     'hen' : Hen,
#     'dog' : Dog,
#     'cow' : Cattle,
#     'suine' : Suine,
#     'horse' : Horse
# }
