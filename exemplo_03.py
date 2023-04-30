""" é feito para embelezar!!! 
Utilizar um valor definido dentro de uma função
em outra função sem passá-lo como parâmetro.

Extremamente útil quando um bloco específico se 
repete dentro de um método específico

Um helper de método.
"""

def soma_x(val_externo):
    """função recebe valor externo
    : é de primeira ordem também
    """
    def interna(val_interno):
        """função recebe um valor interno definido
        : agora o escopo é compartilhado
        """
        return val_externo+val_interno
    return interna

# quando tu chama a soma_x tu ganha a definição de uma nova função, que é a definição interna.
# detalhe* -> com o valor externo preenchido

soma_1 = soma_x(1)
soma_10 = soma_x(10)

print(soma_1(10))
print(soma_10(1))
