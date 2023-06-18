from src.infra.entities import AnimalSex, AnimalTypes
from src.infra.entities import Animals as AnimalsEntity
from src.domain.models import Animals as AnimalsModel

from src.infra.interface.flask_entity_factory import FlaskEntityFactory

class AnimalsEntityFactory(FlaskEntityFactory):
    """Flask utils factory"""

    @classmethod
    def buildEntityByKwargs(cls, **kw):
        return AnimalsEntity(
            name=kw['name'],
            sex=AnimalSex(kw['sex']),
            weight=kw['weight'],
            specie=kw['specie'],
            animal_type=AnimalTypes(kw['animal_type'])
        )

    @classmethod
    def buidlEntityListByKwargsList(cls, kwlist):
        return (
            [(cls.buildEntityByKwargs(
                    name=kwargs['name'],
                    sex=kwargs['sex'],
                    weight=kwargs['weight'] if ('weight' in kwargs) else None,
                    specie=kwargs['specie'] if ('specie' in kwargs) else None,
                    animal_type=kwargs['animal_type']
                )
            ) for kwargs in kwlist]
        )

    @classmethod
    def buildModelInstanceByEntity(cls, enty):
        return AnimalsModel(
            id=enty.id,
            name=enty.name,
            sex=enty.sex.value,
            weight=enty.weight,
            specie=enty.specie,
            animal_type=enty.animal_type.value
        )

    @classmethod
    def buildModelListByEntityList(cls, entylist):
        return (
            [(cls.buildModelInstanceByEntity(anim)) for anim in entylist]
        )
