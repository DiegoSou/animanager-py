from abc import ABC
from functools import wraps
from .call_method import CallMethodAssistant

class ABCFactory(ABC):
    """Adiciona um decorador factory_mtd e atributo mapping que debugga cada método decorado"""
    mapping = {}

    @classmethod
    def factory_mtd(cls, func) -> callable:
        """Define um método da factory"""

        def intermediaria(*args, **kwargs):
            called_func = cls.__call_mtd(func)
            result = called_func(*args, **kwargs)

            if func.__name__ not in cls.mapping:
                cls.mapping[func.__name__] = []

            cls.mapping[func.__name__].append(result)
            return result['data']
        return intermediaria


    @classmethod
    def __call_mtd(cls, func):
        """Chama uma função aplicando o decorador de chamadas"""
        @CallMethodAssistant()
        @wraps(func)
        def intermediaria(*args, **kwargs):
            """Roda a função original"""
            return func(*args, **kwargs)
        return intermediaria
