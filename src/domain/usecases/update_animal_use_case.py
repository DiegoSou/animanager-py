from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Animals

class IUpdateAnimalUseCase(ABC):

    @abstractmethod
    def update_animal(
        self,
        animal_id: str,
        name: str = None,
        weight: str = None,
        specie:str = None
    ) -> Dict[bool, Animals]:
        """
        update an animal record
        - params
            - animal_id: id of animal to update
            - name: update name of animal
            - weight: update weight of animal
            - specie: update specie of animal
        - return
            - Dict {'success':bool, 'data':AnimalsModel}
        """
