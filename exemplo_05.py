# pylint: disable=C0116,C0103
"""
Closure é um caso especial de função
aninhada que armazena variáveis livres

Uma closure pode ser um decorador se:
A função externa receber uma função;
A função recebida é a variável livre;
Retorna a função interna;
"""

# ESCOPO GLOBAL
def decorador(func): # VARIÁVEL DO ESCOPO GLOBAL

    # VARIÁVEL func -> VARIÁVEL EM ESCOPO LOCAL

    def interna(*args): # VARIÁVEL TUPLA DE agrs -> GLOBAL
        resultado = func(*args) # VARIÁVEL LOCAL resultado utiliza da variável local do decorador
        return f"Sou uma closure e sua função returnou {resultado}"

    # No retorno somente a declaração da função interna é retornada,
    # a declaração de func é "solta e fica livre no escopo"
    return interna


def soma(x, y):
    return x+y

decorada = decorador(soma)
print(decorada(1, 2))
