from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Animals

class IRegisterAnimalUseCase(ABC):

    @abstractmethod
    def register_animal(
        self,
        name: str,
        sex: str,
        animal_type: str,
        weight: float = None,
        specie: str = None
    ) -> Dict[bool, Animals]:
        """register an animal record"""
