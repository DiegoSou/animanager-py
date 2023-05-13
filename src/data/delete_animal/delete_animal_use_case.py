from typing import Dict, Type
from src.data.interface import AnimalsRepositoryInterface
from src.domain.models import Animals
from src.domain.usecases import IFindAnimalUseCase, IDeleteAnimalUseCase

class DeleteAnimalUseCase(IDeleteAnimalUseCase):

    def __init__(
            self,
            repo: Type[AnimalsRepositoryInterface],
            find_animal: Type[IFindAnimalUseCase]
        ):
        self.repo = repo
        self.find_animal = find_animal

    def delete_animal(self, animal_id: str) -> Dict[bool, Animals]:

        try:
            animal_old = self.find_animal.find(animal_id=animal_id, convert_to_model=False)['data'][0]

            response = self.repo.animals_delete(animal_old)

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}
