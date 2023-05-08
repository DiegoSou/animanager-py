from src.data import FindAnimalUseCase, RegisterAnimalUseCase
from src.presentation.controllers import FindAnimalController, RegisterAnimalController
from src.infra.repositories import AnimalsRepository

def find_animal_composite():
    """Find animal composite route"""

    repo = AnimalsRepository()
    usecase = FindAnimalUseCase(repo)

    # toda composer retorna uma Controller preenchida com o caso de uso
    # o que libera assim o método route
    controller = FindAnimalController(usecase)
    return controller

def register_animal_composite():
    """Register animal composite route"""

    repo = AnimalsRepository()
    usecase = RegisterAnimalUseCase(repo)

    controller = RegisterAnimalController(usecase)
    return controller
