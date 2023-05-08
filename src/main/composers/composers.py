from src.presentation.controllers import FindAnimalController
from src.infra.repositories import AnimalsRepository
from src.data import FindAnimalUseCase

def find_animal_composite():
    """Find animal composite route"""

    repo = AnimalsRepository()
    usecase = FindAnimalUseCase(repo)

    # toda composer retorna uma Controller preenchida com o caso de uso
    # o que libera assim o método route
    controller = FindAnimalController(usecase)
    return controller
