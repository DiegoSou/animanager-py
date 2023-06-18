from typing import Type, List
from src.infra.entities import AnimalSex, AnimalTypes
from src.infra.entities import Animals as AnimalsEntity
from src.domain.models import Animals as AnimalsModel

from src.utils import ABCFactory

class FlaskAnimalsEntityFactory(ABCFactory):
    """Flask utils factory"""

    @classmethod
    @ABCFactory.factory_mtd
    def buildEntityByKwargs(cls, **kw):
        """constrói um mapeamento de entidade"""
        return AnimalsEntity(
            name=kw['name'],
            sex=AnimalSex(kw['sex']),
            weight=kw['weight'],
            specie=kw['specie'],
            animal_type=AnimalTypes(kw['animal_type'])
        )

    @classmethod
    @ABCFactory.factory_mtd
    def buidlEntityListByKwargsList(cls, kwlist):
        """constrói uma lista de mapeamento de entidade"""
        return (
            [(cls.buildEntityByKwargs(
                    name=kwargs['name'],
                    sex=kwargs['sex'],
                    weight=kwargs['weight'],
                    specie=kwargs['specie'],
                    animal_type=kwargs['animal_type']
                )
            ) for kwargs in kwlist]
        )

    @classmethod
    @ABCFactory.factory_mtd
    def buildModelInstanceByEntity(cls, flask_enty: Type[AnimalsEntity]):
        """constrói uma instancia de animal a partir de um mapeamento de entidade"""
        return AnimalsModel(
            id=flask_enty.id,
            name=flask_enty.name,
            sex=flask_enty.sex.value,
            weight=flask_enty.weight,
            specie=flask_enty.specie,
            animal_type=flask_enty.animal_type.value
        )

    @classmethod
    @ABCFactory.factory_mtd
    def buildModelListByEntityList(cls, flask_enty: List[AnimalsEntity]):
        """constrói uma lista de instancia de animal a partir de uma lista de mapeamento de entidade"""
        return (
            [(cls.buildModelInstanceByEntity(anim)) for anim in flask_enty]
        )
