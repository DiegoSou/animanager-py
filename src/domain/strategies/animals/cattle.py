from src.domain.strategies.interface import AnimalStrategyInterface

class CattleStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para gado"""

    @classmethod
    def action(cls):
        return 'Milk'

    @classmethod
    def competence_param(cls):
        return 'Wheight'
