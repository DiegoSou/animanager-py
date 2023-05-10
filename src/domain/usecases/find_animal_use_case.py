from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Animals

class IFindAnimalUseCase(ABC):

    @abstractmethod
    def find(
        self,
        animal_id: str = None,
        animal_name: str = None,
        animal_type: str = None
    ) -> Dict[bool, List[Animals]]:
        """get animals records by id, name or animal_type"""
