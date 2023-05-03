from typing import Type, Union
from src.infra.factory import FactoryInterface
from src.domain.models import Animals, AnimalTypes
from src.domain.strategies.interface import AnimalStrategyInterface
from src.domain.strategies.animals import (
    HenStrategy,
    DogStrategy,
    CattleStrategy,
    SuineStrategy,
    HorseStrategy,
)


class AnimalFactory(FactoryInterface):
    @classmethod
    @FactoryInterface.factory_method
    def create(cls, name: str, specie: str, weight: float, animal_type: str):
        """Cria modelo de animal"""
        survival_strategy = cls.__define_type(animal_type)

        return Animals(
            name=name,
            specie=specie,
            weight=weight,
            animal_type=AnimalTypes(animal_type),
            survival_strategy=survival_strategy
        )

    @classmethod
    def __define_type(
        cls, animal_type: str
    ) -> Union[Type[AnimalStrategyInterface], None]:
        match animal_type:
            case "hen":
                return HenStrategy
            case "dog":
                return DogStrategy
            case "cattle":
                return CattleStrategy
            case "suine":
                return SuineStrategy
            case "horse":
                return HorseStrategy
        return None
