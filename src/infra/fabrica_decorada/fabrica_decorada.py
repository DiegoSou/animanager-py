from functools import wraps
from src.infra.assistente_de_chamada import AssistentCall as call

class FactoryD:
    """Classe decoradora FactoryD"""

    def __init__(self, name):
        """Construtor para definir uma instância da Factory"""
        self.name = name
        self.mapping = {}
        self.debug_mode = False

    def __call__(self, func):
        """Decorador da factory para registrar histórico de execução do método executado"""

        @call(self.name, self.debug_mode)
        @wraps(func)
        def registry_response(time, *args, **kwargs):
            resultado = func(*args, **kwargs)

            if func.__name__ not in self.mapping:
                self.mapping[func.__name__] = []

            self.mapping[func.__name__].append({ 'time' : time, 'data' : resultado })
            return resultado
 
        return registry_response

    def active_debug(self, activate: bool = True):
        """Ativa/Desativa modo debug para chamadas"""

        self.debug_mode = activate
