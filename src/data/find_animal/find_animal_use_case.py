from typing import Type, Dict, List
from domain.models import Animals
from src.domain.usecases import IFindAnimalUseCase
from src.data.interfaces import AnimalsRepositoryInterface

class FindAnimalUseCase(IFindAnimalUseCase):

    def __init__(self, repo: Type[AnimalsRepositoryInterface]):
        self.repo = repo

    def find_all(self) -> Dict[bool, List[Animals]]:
        response = self.repo.animals_index()

        return {"success": True, "data": response}
