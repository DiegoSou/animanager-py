#pylint:disable=C0116

"""O conceito de poder armazenar funções em qualquer, lugar se chama:
Funções como Objetos de Primeira Classe 
ou
Funções que recebem outras funções e retornam uma função

Funções Aninhadas:
uma função definida dentro de outra função

Mas pra quê?
- Repetir código dentro de uma função
- (que não seria interessante expor e complexo suficiente para separar)
- Encapsulamento
- Escopo 
- (uma função interna pode usar variáveis de funções externas)
"""

def ola(nome):
    def func_internal(nome):
        if nome.lower() == 'marilene':
            print(f"Olá {nome}. A noite, tainha, vinho e muito...")
        else:
            print(f"Olá {nome}, boa noite.")
    func_internal(nome)

ola('Marilene')
