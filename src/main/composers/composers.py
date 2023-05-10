from src.presentation.controllers import (
    FindAnimalController,
    RegisterAnimalController,
    UpdateAnimalController
)
from src.data import FindAnimalUseCase, RegisterAnimalUseCase, UpdateAnimalUseCase
from src.infra.repositories import AnimalsRepository

# manage concretes - agrupa dependências
# toda composer traz um Model (repositório) para os Casos de Uso
# manda o caso de uso para a Controller
# e retorna essa controller com route()

def find_animal_composite():
    """Find animal composite route"""

    repo = AnimalsRepository()
    usecase = FindAnimalUseCase(repo)

    controller = FindAnimalController(usecase)
    return controller


def register_animal_composite():
    """Register animal composite route"""

    repo = AnimalsRepository()
    usecase = RegisterAnimalUseCase(repo)

    controller = RegisterAnimalController(usecase)
    return controller


def update_animal_composite():
    """Update animal composite route"""

    repo = AnimalsRepository()
    usecase = UpdateAnimalUseCase(repo, FindAnimalUseCase(repo))

    controller = UpdateAnimalController(usecase)
    return controller
