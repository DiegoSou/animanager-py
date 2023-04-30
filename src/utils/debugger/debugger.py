from functools import wraps
from datetime import datetime

def debug(verbose = False, level = 0):
    """Decorador debug, que recebe parâmetros"""

    def intermediaria(func):
        """
        Intermediária que armazena variáveis livres.
        Inclusive a "func" é uma delas.
        """
        @wraps(func)
        def decorator(*args, **kwargs):
            """A lógica que abriga uma decoração e executa a função passada
            - params
                - *args: Argumentos posicionais
                - **kwargs: Argumentos nomeados
            - return 
                - o resultado da execução
            """

            print(f"Debug from {__name__}")

            start_t = datetime.now()
            func_result = func(start_t, *args, **kwargs)
            final_t = datetime.now() - start_t

            if verbose:
                print(
                    f"Chamada {func.__name__}\n"
                    f"Parâmetros posicionais: {args}\n"
                    f"Parâmetros nomeados: {kwargs}\n"
                )

            if level > 0:
                print(f"Resultado: {func_result}")
                print(f"Tempo total: {final_t.total_seconds()}\n")
            return func_result
        return decorator
    
    return intermediaria
