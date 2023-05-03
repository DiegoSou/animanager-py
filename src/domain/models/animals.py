from typing import NamedTuple, Type
from enum import Enum
from src.domain.interface import AnimalStrategyInterface

class AnimalSex(Enum):
    FEMALE = 'f'
    MALE = 'm'

class AnimalTypes(Enum):
    HEN = 'hen'
    DOG = 'dog'
    CATTLE = 'cattle'
    SUINE = 'suine'
    HORSE = 'horse'

class Animals(NamedTuple):
    name: str
    specie: str
    weight: float
    animal_type: Type[AnimalTypes]
    survival_strategy: Type[AnimalStrategyInterface]
