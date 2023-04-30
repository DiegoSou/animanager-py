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
        """
        Constrói o assistente de chamadas de uma factory
        - params:
            - debug_mode: mostra estatísticas da execução do método
        """
        self.from_factory = from_factory
        self.__active_debug(debug_mode)

    def __call__(self, func):
        """
        Define que instâncias da classe serão chamadas recebendo uma função como parâmetro
        (no caso a registry call da factory) \n
        Define utilitários aplicados na chamada:
        - debug
        """

        @self.debugger
        @wraps(func)
        def intermediario(*args, **kwargs):
            print(f"Criado(a) pela fábrica: {self.from_factory}")
            print(f"Chamado(a) pela função: {func.__name__}")
            return func(*args, **kwargs) # debugger vai colocar datetime de execução nos args
        return intermediario


    def __active_debug(self, active: bool = False):
        if active:
            self.debugger = debug(verbose=True, level=1)
        else:
            self.debugger = debug(verbose=False, level=0)
