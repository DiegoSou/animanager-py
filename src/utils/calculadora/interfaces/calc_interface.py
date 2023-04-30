"""Interface de verificação dos parâmetros de uma calculadora"""

def autentica_calculadora(param_list, params_type):
    """Verificações dos tipos dos parametros"""

    def verifica_tipo(param : any, tipo : str) -> bool:
        """Verifica o tipo de um único parâmetro"""
        valido = False
        match tipo:
            case 'int':
                valido = isinstance(param, int)
            case 'float':
                valido = isinstance(param, float)
            case 'string':
                valido = isinstance(param, str)
            case 'bool':
                valido = isinstance(param, bool)
            case 'tuple':
                valido = isinstance(param, tuple)
            case 'list':
                valido = isinstance(param, list)
            case 'dict':
                valido = isinstance(param, dict)
        return valido

    if not verifica_tipo(param_list, 'tuple'):
        print("Lista dos parâmetros deve ser tupla!")
        return False

    for param in param_list:
        if not verifica_tipo(param, params_type):
            print(f"Devem ser apenas números {params_type}")
            return False

    return True
