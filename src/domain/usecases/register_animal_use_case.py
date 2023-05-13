from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Animals

class IRegisterAnimalUseCase(ABC):

    @abstractmethod
    def register_animal(
        self,
        name: str,
        sex: str,
        animal_type: str,
        weight: float = None,
        specie: str = None
    ) -> Dict[bool, Animals]:
        """
        register an animal record
        - params
            - animal informations
        - return
            - Dict {'success':bool, 'data':AnimalsModel}
        """

    @abstractmethod
    def upload_animals(
        self,
        csv_data: any
    ) -> Dict[bool, List[Animals]]:
        """
        upload animals from file
        - params
            - animals csv data
        - return
            - Dict {'success':bool, 'data':List of AnimalsModel}
        """
