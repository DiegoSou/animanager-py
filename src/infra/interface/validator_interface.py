from abc import ABC, abstractmethod

class ValidatorInterface(ABC):
    """Interface para agentes de validação"""

    def __init__(self, handler: str):
        """
        Constructor
        - params
            - handler: serviço desejado para a validação do parâmetro
        """
        # vai permitir que tenhamos uma instância de um validador que mude
        # a validação e ação de acordo com o serviço desejado
        self.handler = handler

    @abstractmethod
    def validate(self, param: any) -> bool:
        """Validação de um argumento com base no serviço"""

    @abstractmethod
    def action(self):
        """Ação ao ser validado com base no serviço"""
