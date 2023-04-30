""" Um exemplo útil 
- nested functions
"""

from unicodedata import normalize

def normaliza(*palavras):
    """func - normaliza"""
    saida = []

    for palavra in palavras:
        normalizado = normalize('NFKD', palavra)
        normalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')

        saida.append(normalizada)

    return saida

def normaliza2(*palavras):
    """ func - normaliza_2 
    for simplificadoo
    """

    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return (normalizado.encode('ASCII', 'ignore').decode('ASCII'))

    return [ajudante(palavra) for palavra in palavras]

print(normaliza('Érico', 'Sabiá', 'João'), '\n')
print(normaliza2('Érico', 'Sabiá', 'João'), '\n')
