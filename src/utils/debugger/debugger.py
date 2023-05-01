from datetime import datetime
from functools import wraps

def debug():
    """Decorador debug, que recebe parâmetros"""

    def execute(func):
        """Executa a chamada da função
        * Mede o tempo de duração da chamada
        """
        @wraps(func)
        def intermediaria(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            total_time = datetime.now() - start_time

            return {
                'start': start_time.strftime('%d/%m/%Y, %H:%M:%S'),
                'duration': total_time.total_seconds(),
                'data': result 
            }
        return intermediaria

    def get_args(func):
        """Mostra os argumentos da função"""
        def intermediaria(*args, **kwargs):
            print(
                f"Method name: {func.__name__}\n"
                f"Positional params: {args}\n"
                f"Named params: {kwargs}\n"
            )
            return func(*args, **kwargs)
        return intermediaria


    def run_debug(func):
        """Intermediária que recebe variáveis livres."""
        @get_args
        @execute
        @wraps(func)
        def intermediaria(*args, **kwargs):
            """
            A lógica que abriga uma decoração e executa a função passada
            - params
                - *args: Argumentos posicionais
                - **kwargs: Argumentos nomeados
            - return 
                - o resultado da execução
            """
            return func(*args, **kwargs)
        return intermediaria

    return run_debug
