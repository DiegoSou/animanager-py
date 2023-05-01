from abc import ABC
from functools import wraps
from src.infra.config.call_method_config import CallMethodInterface

class FactoryInterface(ABC):
    """Interface decoradora para fábricas"""
    mapping = {}

    @classmethod
    def __get_classname(cls):
        return cls.__name__

    @classmethod
    def factory_method(cls, func) -> callable:
        """Instâncias da factory viram um callable"""
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
        @CallMethodInterface(cls.__get_classname())
        @wraps(func)
        def intermediaria(*args, **kwargs):
            """Roda a função original"""
            return func(*args, **kwargs)
        return intermediaria
