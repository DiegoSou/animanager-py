from typing import Type, Dict
from src.data.interface import AnimalsRepositoryInterface
from src.domain.models import Animals
from src.domain.usecases import IFindAnimalUseCase, IUpdateAnimalUseCase

class UpdateAnimalUseCase(IUpdateAnimalUseCase):

    def __init__(
            self,
            repo: Type[AnimalsRepositoryInterface],
            find_animal: Type[IFindAnimalUseCase]
        ):
        self.repo = repo
        self.find_animal = find_animal

    def update_animal(
            self,
            animal_id: str,
            name: str = None,
            weight: float = None,
            specie: str = None
        ) -> Dict[bool, Animals]:

        try:
            animal_old = self.find_animal.find(animal_id=animal_id, convert_to_model=False)['data'][0]

            response = self.repo.animals_update(
                animal_old=animal_old,
                name=name,
                weight=weight,
                specie=specie
            )

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}
