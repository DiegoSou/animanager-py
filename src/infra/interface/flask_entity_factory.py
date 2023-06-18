from abc import abstractmethod

from src.utils import ABCFactory

class FlaskEntityFactory(ABCFactory):
    """Flask utils factory"""

    @classmethod
    @ABCFactory.factory_mtd
    @abstractmethod
    def buildEntityByKwargs(cls, **kw):
        """constrói um mapeamento de entidade"""

    @classmethod
    @ABCFactory.factory_mtd
    @abstractmethod
    def buidlEntityListByKwargsList(cls, kwlist):
        """constrói uma lista de mapeamento de entidade"""

    @classmethod
    @ABCFactory.factory_mtd
    @abstractmethod
    def buildModelInstanceByEntity(cls, enty):
        """constrói uma instancia de modelo a partir de um mapeamento de entidade"""

    @classmethod
    @ABCFactory.factory_mtd
    @abstractmethod
    def buildModelListByEntityList(cls, entylist):
        """constrói uma lista de instancia de modelo a partir de uma lista de mapeamento de entidade"""
