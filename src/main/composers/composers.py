from src.presentation.controllers import FindAnimalController
from src.infra.repositories import AnimalsRepository
from src.data import FindAnimalUseCase

def find_animal_composite():
    """Find animal composite route"""

    repo = AnimalsRepository()
    usecase = FindAnimalUseCase(repo)
    controller = FindAnimalController(usecase)
    return controller
