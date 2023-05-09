from typing import Dict, Type
from src.domain.models import Animals
from src.data.interface import AnimalsRepositoryInterface
from src.domain.usecases import IRegisterAnimalUseCase

class RegisterAnimalUseCase(IRegisterAnimalUseCase):

    def __init__(self, repo: Type[AnimalsRepositoryInterface]):
        self.repo = repo

    def register_animal(
            self,
            name: str,
            sex: str,
            animal_type: str,
            weight: float = None,
            specie: str = None
        ) -> Dict[bool, Animals]:

        try:
            response = self.repo.animals_register(
                name=name,
                sex=sex,
                weight=weight,
                specie=specie,
                animal_type=animal_type
            )

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "data": exc}
