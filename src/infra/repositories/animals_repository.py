from typing import List
from src.domain.models import Animals as AnimalsModel
from src.infra.entities import Animals as AnimalsEntity
from src.data.interfaces import AnimalsRepositoryInterface

class AnimalsRepository(AnimalsRepositoryInterface):

    def animals_index(self) -> List[AnimalsModel]:
        result_query = AnimalsEntity.query.all()
        animals = []

        for entity in result_query:
            animals.append(
                AnimalsModel(
                    id=entity.id,
                    name=entity.name,
                    sex=entity.sex.value,
                    weight=entity.weight,
                    specie=entity.specie,
                    animal_type=entity.animal_type.value
                )
            )
        return animals
