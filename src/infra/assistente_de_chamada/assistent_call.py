"""Classe decoradora c"""
from functools import wraps
from src.utils.debugger import debug

class AssistentCall:
    """
    Classe decoradora: Define regras para chamadas de métodos
    - métodos:
        - __init__: define uma instância, é o construtor
        - __call__: será executado toda vez que a instância for chamada como uma função
    """
    def __init__(self, from_factory: str, debug_mode: bool):
        self.from_factory = from_factory
        self.debugger = debug(verbose=True, level=1) if debug_mode else debug()

    def __call__(self, func):
        """Coloca utilitários da execução aqui"""
        @self.debugger
        @wraps(func)
        def intermediario(*args, **kwargs):
            print(f"Criado(a) pela fábrica: {self.from_factory}")
            print(f"Chamado(a) pela função: {func.__name__}")
            return func(*args, **kwargs)
        return intermediario
