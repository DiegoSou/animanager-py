from abc import ABC
from functools import wraps
from src.utils.call_method import CallMethodAssistant

class FactoryInterface(ABC):
    """Interface decoradora para fábricas"""
    mapping = {}

    @classmethod
    def factory_method(cls, func) -> callable:
        """Define um método da factory"""

        def intermediaria(*args, **kwargs):
            called_func = cls.__call_method(func)
            result = called_func(*args, **kwargs)

            if func.__name__ not in cls.mapping:
                cls.mapping[func.__name__] = []

            cls.mapping[func.__name__].append(result)
            return result['data']
        return intermediaria


    @classmethod
    def __call_method(cls, func):
        """Chama uma função aplicando o decorador de chamadas"""
        @CallMethodAssistant()
        @wraps(func)
        def intermediaria(*args, **kwargs):
            """Roda a função original"""
            return func(*args, **kwargs)
        return intermediaria
