from src.infra.factory_config import FactoryInterface
from src.infra.call_method_config import CallMethodInterface

animal_factory = FactoryInterface('AnimalFactory', CallMethodInterface)
@animal_factory
def create_animal(name):
    """cria um animal"""
    return { 'animal' : name }


bixo = create_animal('Dog')
print(bixo)
print(animal_factory.mapping)


# from src.infra.factory_config import FactoryD
# from src.domain.models.Animals import Hen

# (é só um exemplo)
# fabrica_animal = FactoryD('Animal\'s')
# fabrica_animal.active_debug()

# @fabrica_animal
# def create_hen(name: str, eggs_per_week: int):
#     """Hen põe ovos"""
#     if eggs_per_week < 4:
#         return None

#     return Hen(name=name, eggs_per_week=eggs_per_week)

# create_hen(name='Faca', eggs_per_week=5)
# create_hen('Hennrick', 7)
# create_hen('Joe', 2)
# create_hen('Kell', 4)

# print(fabrica_animal.mapping)
