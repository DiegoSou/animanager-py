from typing import List
from src.domain.models import Animals as AnimalsModel
from src.infra.entities import AnimalSex, AnimalTypes
from src.infra.entities import Animals as AnimalsEntity
from src.data.interface import AnimalsRepositoryInterface

from src.main.app_config import db

class AnimalsRepository(AnimalsRepositoryInterface):

    def animals_select(self, animal_id, animal_name, animal_type) -> List[AnimalsModel]:

        if animal_id:
            result_query = AnimalsEntity.query.filter_by(id=animal_id).first()

        elif animal_name and not animal_type:
            result_query = AnimalsEntity.query.filter_by(name=animal_name).all()

        elif not animal_name and animal_type:
            result_query = AnimalsEntity.query.filter_by(animal_type=animal_type).all()

        elif animal_name and animal_type:
            result_query = AnimalsEntity.query.filter_by(name=animal_name, animal_type=animal_type).all()

        else: result_query = AnimalsEntity.query.all()

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
                sex=AnimalSex(sex),
                weight=weight,
                specie=specie,
                animal_type=AnimalTypes(animal_type)
            )
        )

        db.session.add(result_insert)
        db.session.commit()

        return AnimalsModel(
            id=result_insert.id,
            name=result_insert.name,
            sex=result_insert.sex.value,
            weight=result_insert.weight,
            specie=result_insert.specie,
            animal_type=result_insert.animal_type.value
        )


    def animals_update(self, animal_id, name, weight, specie) -> str:
        result_update = (
            AnimalsEntity(
                id=animal_id,
                name=name,
                weight=weight,
                specie=specie
            )
        )

        db.session.add(result_update)
        db.session.commit()

        return animal_id
