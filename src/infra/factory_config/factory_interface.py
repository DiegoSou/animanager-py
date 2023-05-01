from abc import ABC
from functools import wraps

class FactoryInterface(ABC):
    """Interface decoradora para fábricas"""

    def __init__(self, name: str, call_interface: callable):
        """Construtor para definir uma instância da Factory"""
        self.name = name
        self.mapping = {}
        self.call_interface = call_interface(self.name)

    def factory_method(self, func) -> callable:
        """Instâncias da factory viram um callable"""
        def intermediaria(*args, **kwargs):
            called_func = self.__call_method(func)
            result = called_func(*args, **kwargs)

            if func.__name__ not in self.mapping:
                self.mapping[func.__name__] = []

            self.mapping[func.__name__].append(result)
            return result['data']
        return intermediaria

    def __call_method(self, func):
        """Chama uma função aplicando o decorador de chamadas"""
        @self.call_interface
        @wraps(func)
        def intermediaria(*args, **kwargs):
            """Roda a função original"""
            return func(*args, **kwargs)
        return intermediaria
