# pylint: disable=C0116
"""
Closure é um caso especial de função
aninhada que armazena variáveis livres

Uma closure pode ser um decorador se:
A função externa receber uma função;
A função recebida é a variável livre;
Retorna a função interna;
"""

def decorador(func):

    def interna(*args):
        resultado = func(*args)
        return f"Sou uma closure e sua função returnou {resultado}"

    return interna
