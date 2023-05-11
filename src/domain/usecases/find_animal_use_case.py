from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Animals

class IFindAnimalUseCase(ABC):

    @abstractmethod
    def find(
        self,
        animal_id: str = None,
        animal_name: str = None,
        animal_type: str = None,
        convert_to_model: bool = True
    ) -> Dict[bool, List[Animals]]:
        """
        get animals records
        - params
            - animal_id: get by id
            - animal_name: get by name
            - animal_type: get by animal type
        - return
            - Dict {'success':bool, 'data':List[AnimalsModel or AnimalsEntity]}
        """
