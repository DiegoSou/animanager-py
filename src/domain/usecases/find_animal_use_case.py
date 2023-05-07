from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Animals

class IFindAnimalUseCase(ABC):

    @abstractmethod
    def find_all(self) -> Dict[bool, List[Animals]]:
        """get all animals records"""
