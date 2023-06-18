from src.presentation.controllers import (
    FindAnimalController,
    RegisterAnimalController,
    UpdateAnimalController,
    DeleteAnimalController
)
from src.data import (
    FindAnimalUseCase,
    RegisterAnimalUseCase,
    UpdateAnimalUseCase,
    DeleteAnimalUseCase,
    AnimalsEntityFactory
)
from src.infra.repositories import AnimalsRepository

# manage concretes - agrupa dependências
# toda composer traz um Model (MVC) (no caso o repositório) para os Casos de Uso
# manda o Caso de Uso (com o Model) para a Controller
# e retorna essa Controller com método route() implementado

repo = AnimalsRepository(entity_factory=AnimalsEntityFactory)

def find_animal_composite():
    """Find animal composite route"""

    usecase = FindAnimalUseCase(repo)
    controller = FindAnimalController(usecase)
    return controller


def register_animal_composite():
    """Register animal composite route"""

    usecase = RegisterAnimalUseCase(repo)
    controller = RegisterAnimalController(usecase)
    return controller


def update_animal_composite():
    """Update animal composite route"""

    usecase = UpdateAnimalUseCase(repo, FindAnimalUseCase(repo))
    controller = UpdateAnimalController(usecase)
    return controller

def delete_animal_composite():
    """Delete animal composite route"""

    usecase = DeleteAnimalUseCase(repo, FindAnimalUseCase(repo))
    controller = DeleteAnimalController(usecase)
    return controller
