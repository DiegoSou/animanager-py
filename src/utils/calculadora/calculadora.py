#pylint:disable=C0103
"""Funções são objetos"""
from collections import namedtuple

Func = namedtuple("callable", "execute")

def pega_comprimento(algo_com_comprimento) -> int:
    """Pega o length do que for passado como parâmetro"""
    return (len(algo_com_comprimento)) if algo_com_comprimento else 'Não disponível para nulo.'

def calculadora(
        authenticator_interface : callable,
        operador : str,
        nums_tuple : tuple,
        nums_type : str
    ):
    """
    Calculadora!
    - params 
        - auth_interface: método interface para verificação (tipo dos parametros, parametros)
        - operador: '+,-,/,*'
        - x: primeiro número
        - y: segundo número
    - return 
        - resposta da operação
    """
    operacoes = {
        '+' : (lambda x,y : x+y),
        '-' : (lambda x,y : x-y),
        '*' : (lambda x,y : x*y),
        '/' : (lambda x,y : x/y)
    }

    if not authenticator_interface(nums_tuple, nums_type):
        return None

    retorno = 0
    for indx, _ in enumerate(nums_tuple):
        if indx < (len(nums_tuple)-1):
            retorno = (
                operacoes[operador](nums_tuple[indx], nums_tuple[indx+1]) if
                retorno == 0 else operacoes[operador](retorno, nums_tuple[indx+1])
            )

    return retorno
