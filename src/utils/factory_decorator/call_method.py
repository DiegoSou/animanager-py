from functools import wraps
from .debugger import debug

class CallMethodAssistant:
    """
    Assistente para definir regras para chamadas de métodos
    - métodos:
        - __init__: construtor
        - __call__: instância da classe vira um callable
    """

    def __init__(self):
        """define os decoradores para as chamadas"""
        self.debugger = debug()

    def __call__(self, func):
        """
        Enrola uma função com decoradores assistentes de chamada:
        - debug
        """
        @self.debugger
        @wraps(func)
        def intermediaria(*args, **kwargs) -> callable:
            print(f'Called Method from {args[0].__name__}')
            return func(*args, **kwargs)
        return intermediaria
