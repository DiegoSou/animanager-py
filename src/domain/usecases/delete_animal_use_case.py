from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Animals

class IDeleteAnimalUseCase(ABC):

    @abstractmethod
    def delete_animal(self, animal_id: str) -> Dict[bool, Animals]:
        """
        delete an animal record
        - params
            - animal_id: id of animal to delete
        - return
            - Dict {'success':bool, 'data':AnimalsModel}
        """
