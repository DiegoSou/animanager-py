from functools import wraps
from src.infra.assistente_de_chamada import AssistentCall as call

class FactoryD:
    """
    Classe decoradora Factory_d
    - métodos:
        - __init__: define uma instância de D e constrói uma instância de C, é o construtor
        - __call__: executa métodos com a instância de C e salva no mapeamento 
                    (cria um histórico de execução para cada método que a fábrica chamou)
    """
    def __init__(self, name):
        self.name = name
        self.mapping = {}
        self.debug_mode = False

    def __call__(self, func):
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
