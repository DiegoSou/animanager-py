from typing import Type, Dict
from src.data.interface import AnimalsRepositoryInterface
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
        ) -> Dict[bool, str]:

        try:
            animal_old = self.find_animal.find(animal_id=animal_id)['data'][0]

            animal_old.name = name if name else animal_old.name
            animal_old.weight = weight if weight else animal_old.weight
            animal_old.specie = specie if specie else animal_old.specie

            response = self.repo.animals_update(
                animal_id=animal_old.id,
                name=animal_old.name,
                specie=animal_old.specie
            )

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "data": exc}
