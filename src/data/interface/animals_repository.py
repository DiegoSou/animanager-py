from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Animals

class AnimalsRepositoryInterface(ABC):

    @abstractmethod
    def animals_index(self) -> List[Animals]:
        """get all animals records"""

    @abstractmethod
    def animals_register(self, name, sex, weight, specie, animal_type) -> Animals:
        """register an animal record"""
