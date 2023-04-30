# pylint:disable=C0103,C0114,c0305,w0719
"""decorador recebendo parâmetros!"""

def retry(erro, vezes):
    """função que repete caso erro"""
    count = 0 #variavel livre

    def intermediaria(func):

        def closure(*args, **kwargs):
            nonlocal count

            try:
                return func(*args, **kwargs)
            except erro as e:
                count += 1
                print(f"{func.__name__} error: {e} retry: {count}")

                if count < vezes:
                    return closure(*args, **kwargs)
        return closure
    return intermediaria

@retry(Exception, 5)
def nao_pode_receber_parametro(param: any = None):
    """função que dá errado se receber parâmetro"""
    if param:
        raise Exception('Exception raised.')

    print("Não tem parâmetro.")
