from functools import wraps
from src.utils.debugger import debug

class CallMethodInterface:
    """
    Classe decoradora: Define regras para chamadas de métodos
    - métodos:
        - __init__: define uma instância, é o construtor
        - __call__: será executado toda vez que a instância for chamada como uma função
    """

    def __init__(self, from_factory: str):
        """
        Constrói o assistente de chamadas de uma factory
        - params:
            - debug_mode: mostra estatísticas da execução do método
        """
        self.from_factory = from_factory
        self.debugger = debug()

    def __call__(self, func):
        """
        Enrola uma função com decoradores assistentes de chamada:
        - debug
        """
        @self.debugger
        @wraps(func)
        def intermediaria(*args, **kwargs) -> callable:
            print(f'Called Method from {self.from_factory}')
            return func(*args, **kwargs)
        return intermediaria
