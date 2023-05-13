from typing import Type, Dict, List
from src.domain.models import Animals
from src.domain.usecases import IFindAnimalUseCase
from src.data.interface import AnimalsRepositoryInterface

class FindAnimalUseCase(IFindAnimalUseCase):

    def __init__(self, repo: Type[AnimalsRepositoryInterface]):
        self.repo = repo

    def find(
            self,
            animal_id: str = None,
            animal_name: str = None,
            animal_type: str = None,
            convert_to_model: bool = True
        ) -> Dict[bool, List[Animals]]:

        try:
            response = self.repo.animals_select(animal_id, animal_name, animal_type, convert_to_model)

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}
