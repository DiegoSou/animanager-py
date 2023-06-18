from src.data.interface import AnimalsRepositoryInterface

from src.main.app_config import db
from src.infra.entities import Animals as AnimalsEntity
from src.infra.interface import FlaskEntityFactory as EntityFactoryInterface

class AnimalsRepository(AnimalsRepositoryInterface):

    def __init__(self, entity_factory: EntityFactoryInterface):
        self.animals_entity_factory = entity_factory


    def animals_select(
            self,
            animal_id,
            animal_name,
            animal_type,
            convert_to_model
        ):

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

        return (
            self.animals_entity_factory.buildModelListByEntityList(result_query)
            if convert_to_model
            else
            result_query
        )


    def animals_register(self, name, sex, weight, specie, animal_type):
        entity = self.animals_entity_factory.buildEntityByKwargs(
            name=name,
            sex=sex,
            weight=weight,
            specie=specie,
            animal_type=animal_type
        )

        db.session.add(entity)
        db.session.commit()

        return self.animals_entity_factory.buildModelInstanceByEntity(entity)


    def animals_bulk_register(self, animals_data):
        entities = self.animals_entity_factory.buidlEntityListByKwargsList(animals_data)

        db.session.add_all(entities)
        db.session.commit()

        return self.animals_entity_factory.buildModelListByEntityList(entities)


    def animals_update(self, animal_old, name, weight, specie):
        animal_old.name = name
        animal_old.weight = weight
        animal_old.specie = specie

        db.session.add(animal_old)
        db.session.commit()

        return self.animals_entity_factory.buildModelInstanceByEntity(animal_old)


    def animals_delete(self, animal_old):
        db.session.delete(animal_old)
        db.session.commit()

        return self.animals_entity_factory.buildModelInstanceByEntity(animal_old)
