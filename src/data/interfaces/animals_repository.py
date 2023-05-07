from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Animals

class AnimalsRepositoryInterface(ABC):

    @abstractmethod
    def animals_index(self) -> List[Animals]:
        """get all animals records"""
