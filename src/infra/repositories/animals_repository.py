from typing import List
from src.domain.models import Animals as AnimalsModel
from src.infra.entities import AnimalSex, AnimalTypes
from src.infra.entities import Animals as AnimalsEntity
from src.data.interface import AnimalsRepositoryInterface

from src.main.app_config import db

class AnimalsRepository(AnimalsRepositoryInterface):

    def animals_select(
            self,
            animal_id,
            animal_name,
            animal_type,
            convert_to_model
        ) -> List[AnimalsModel]:

        if animal_id:
            result_query = [AnimalsEntity.query.filter_by(id=animal_id).first()]

        elif animal_name and not animal_type:
            result_query = AnimalsEntity.query.filter_by(name=animal_name).all()

        elif not animal_name and animal_type:
            result_query = AnimalsEntity.query.filter_by(animal_type=animal_type).all()

        elif animal_name and animal_type:
            result_query = AnimalsEntity.query.filter_by(
                name=animal_name,
                animal_type=animal_type
            ).all()

        else: result_query = AnimalsEntity.query.all()

        if not convert_to_model:
            return result_query

        return [
            AnimalsModel(
                id=anim.id,
                name=anim.name,
                sex=anim.sex.value,
                weight=anim.weight,
                specie=anim.specie,
                animal_type=anim.animal_type.value
            )
            for anim in result_query
        ]


    def animals_register(self, name, sex, weight, specie, animal_type) -> AnimalsModel:
        entities = AnimalsEntity(
            name=name,
            sex=AnimalSex(sex),
            weight=weight,
            specie=specie,
            animal_type=AnimalTypes(animal_type)
        )
        

        db.session.add(entities)
        db.session.commit()

        return AnimalsModel(
            id=entities.id,
            name=entities.name,
            sex=entities.sex.value,
            weight=entities.weight,
            specie=entities.specie,
            animal_type=entities.animal_type.value
        )

    def animals_bulk_register(self, animals_data) -> List[AnimalsModel]:
        entities = []

        for idx in animals_data.index:

            weight = animals_data['weight'][idx] if ('weight' in animals_data.columns) else None
            specie = animals_data['specie'][idx] if ('specie' in animals_data.columns) else None

            entities.append(
                AnimalsEntity(
                    name=animals_data['name'][idx],
                    sex=AnimalSex(animals_data['sex'][idx]),
                    weight=weight,
                    specie=specie,
                    animal_type=AnimalTypes(animals_data['animal_type'][idx])
                )
            )

        db.session.add_all(entities)
        db.session.commit()

        return [
            AnimalsModel(
                id=anim.id,
                name=anim.name,
                sex=anim.sex.value,
                weight=anim.weight,
                specie=anim.specie,
                animal_type=anim.animal_type.value
            )
            for anim in entities
        ]

    def animals_update(self, animal_old, name, weight, specie) -> AnimalsModel:
        animal_old.name = name
        animal_old.weight = weight
        animal_old.specie = specie

        db.session.add(animal_old)
        db.session.commit()

        return AnimalsModel(
            id=animal_old.id,
            name=animal_old.name,
            sex=animal_old.sex.value,
            weight=animal_old.weight,
            specie=animal_old.specie,
            animal_type=animal_old.animal_type.value
        )

    def animals_delete(self, animal_old) -> AnimalsModel:
        db.session.delete(animal_old)
        db.session.commit()

        return AnimalsModel(
            id=animal_old.id,
            name=animal_old.name,
            sex=animal_old.sex.value,
            weight=animal_old.weight,
            specie=animal_old.specie,
            animal_type=animal_old.animal_type.value
        )
