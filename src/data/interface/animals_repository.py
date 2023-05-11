from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Animals

class AnimalsRepositoryInterface(ABC):

    @abstractmethod
    def animals_select(
        self,
        animal_id,
        animal_name,
        animal_type,
        convert_to_model
        ) -> List[Animals]:
        """get animals records by id, name or animal_type"""

    @abstractmethod
    def animals_register(self, name, sex, weight, specie, animal_type) -> Animals:
        """register an animal record"""

    @abstractmethod
    def animals_update(self, animal_old, name, weight, specie) -> Animals:
        """update an old animal record"""
