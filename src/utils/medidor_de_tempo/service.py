#pylint:disable=C0114, C0116
from datetime import datetime

def medidor_de_tempo(func):
    """Função de ordem superior (recebe ou retorna função de primeira classe)"""

    def aninhada(*args, **kwargs):
        """Função Aninhada (está dentro de outra função)"""

        tempo_inicial = datetime.now()

        resultado = func(*args, **kwargs)

        tempo_final = datetime.now()
        tempo = tempo_final - tempo_inicial

        print(f"{func.__name__} demorou {tempo.total_seconds()} segundos.")
        return resultado

    return aninhada
