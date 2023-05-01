from datetime import datetime

def debug():
    """Decorador debug, que recebe parâmetros"""

    def get_time(func):
        """Mede tempo de chamada da função
        * irá rodar a função
        """
        def intermediaria(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            total_time = datetime.now() - start_time

            # To-do: data deve ser json 
            return { 'start': start_time, 'duration': total_time, 'data': result }
        return intermediaria

    def get_args(func):
        """Mostra os argumentos da função"""
        def intermediaria(*args, **kwargs):
            print(
                f"Chamada {func.__name__}\n"
                f"Parâmetros posicionais: {args}\n"
                f"Parâmetros nomeados: {kwargs}\n"
            )
            return func(*args, **kwargs)
        return intermediaria


    def run_debug(func):
        """Intermediária que recebe variáveis livres."""
        @get_args
        @get_time
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
