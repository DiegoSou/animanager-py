from src.domain.strategies.interface import AnimalStrategyInterface

class SuineStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para porco"""

    @classmethod
    def action(cls):
        return 'Eat'

    @classmethod
    def competence_param(cls):
        return 'Wheight'
