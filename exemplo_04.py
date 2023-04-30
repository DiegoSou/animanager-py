# pylint:disable=C0116
"""exemplo usando uma clousure"""

def contador(start=0):
    """count é uma variável definida dentro de contador"""
    count = start

    def interna():
        """ interna é uma clousure
        : se count fosse declarado no escopo local de interna,
          ele seria redefinido a cada chamada.
        """
        nonlocal count # variável livre
        count += 1
        return count
    return interna

c = contador()
print(c.__closure__)
print(c.__closure__[0].cell_contents)
print(c.__code__.co_freevars)
print(c.__code__.co_filename)
