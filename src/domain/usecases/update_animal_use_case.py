from abc import ABC, abstractmethod
from typing import Dict

class IUpdateAnimalUseCase(ABC):

    @abstractmethod
    def update_animal(
        self,
        animal_id: str,
        name: str = None,
        weight: str = None,
        specie:str = None
    ) -> Dict[bool, str]:
        """update an animal record"""
