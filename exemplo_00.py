# pylint: disable=W0105
'''
Funções são objetos*

Decoradores - Anotações:
Os decoradores são bem flexiveis em relação a sua usabilidade.
No primeiro exemplo foi usado para contar o tempo de duração de uma função
- respeitando um período de (a função iniciou) até (a função parou) por exemplo
- sem essa de executar o decorador antes ou depois de uma função
No segundo exemplo foi usado como uma espécie de condição para a função ser executada
ou não, ou seja, antes de executar: @cache

Podemos colocar vários decoradores, basta quebrar linha entre eles

Texto motivador e direcionador:
Decoradores são um açucar refinado para o funcionamento de closures.
Closures são um caso especial de aninhamento de funções de ordem superior 
    que armazenam variáveis livres.
Funções aninhadas são funções definidas dentro de funções.
Funções de ordem superior são funções que podem receber ou retornar funções de primeira classe.
Funções de primeira classe são funções como objetos, assim como fazemos no javascript,
    elas podem ser colocadas em variáveis, 
    colocadas em containers e 
    passadas/retornadas por funções.
Variáveis livres são variáveis que não pertencem ao escopo global ou local.
'''

from time import sleep
from functools import cache
# from medidor_de_tempo import medidor_de_tempo

# @medidor_de_tempo
@cache
def delay(secs):
    """Dorme o terminal"""
    sleep(secs)
    print_em_um_numero(secs)
    return secs

def print_em_um_numero(num):
    """Printa um numero"""
    print('Printando: ' + str(num))

# não vai demorar 30 segundos
print(delay(5), delay(5), delay(5))
