from abc import ABC, abstractmethod

class ValidatorInterface(ABC):
    """Interface para agentes de validação"""

    @abstractmethod
    def validate(self, param: any) -> bool:
        """Validação de um argumento"""

    @abstractmethod
    def action(self):
        """Ação ao ser validado"""
