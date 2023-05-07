from abc import ABC, abstractmethod

class ResponsabilityInterface(ABC):
    """Interface para agentes de validação"""

    def __init__(self, scenario: str):
        """
        Constructor
        - params
            - scenario: o cenário que ocorre a validação (ex: hunt - valida uma presa)
        """
        self.scenario = scenario

    @abstractmethod
    def validate(self, param: any) -> bool:
        """Validação de um argumento"""

    @abstractmethod
    def action(self):
        """Ação ao ser validado"""
