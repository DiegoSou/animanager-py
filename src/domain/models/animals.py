from typing import NamedTuple, Type
from enum import Enum
from src.domain.interface import AnimalStrategyInterface
from src.infra.chain_responsability import ValidatorInterface

class AnimalSex(Enum):
    FEMALE = 'f'
    MALE = 'm'

class AnimalTypes(Enum):
    HEN = 'hen'
    DOG = 'dog'
    CATTLE = 'cattle'
    PIG = 'pig'
    HORSE = 'horse'

class Animals(NamedTuple):
    name: str
    specie: str
    weight: float
    animal_type: Type[AnimalTypes]
    survival_strategy: Type[AnimalStrategyInterface]
    diet_validation : Type[ValidatorInterface]
