from typing import List
from src.domain.models import Animals as AnimalsModel
from src.infra.entities import Animals as AnimalsEntity
from src.data.interfaces import AnimalsRepositoryInterface

from src.main.app_config import db

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

    def animals_register(self, name, sex, weight, specie, animal_type) -> AnimalsModel:
        result_insert = (
            AnimalsEntity(
                name=name,
                sex=sex,
                weight=weight,
                specie=specie,
                animal_type=animal_type
            )
        )

        db.session.add(result_insert)
        db.session.commit()

        return AnimalsModel(
            id=result_insert.id,
            name=result_insert.name,
            sex=result_insert.sex,
            weight=result_insert.weight,
            specie=result_insert.specie,
            animal_type=result_insert.animal_type
        )
