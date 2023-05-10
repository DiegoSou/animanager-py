from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Animals

class AnimalsRepositoryInterface(ABC):

    @abstractmethod
    def animals_select(self, animal_id, animal_name, animal_type) -> List[Animals]:
        """get animals records by id, name or animal_type"""

    @abstractmethod
    def animals_register(self, name, sex, weight, specie, animal_type) -> Animals:
        """register an animal record"""
