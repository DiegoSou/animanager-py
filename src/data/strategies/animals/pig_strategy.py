from src.domain.interface import AnimalStrategyInterface

class PigStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para porco"""

    @classmethod
    def action(cls):
        return 'Eat'

    @classmethod
    def competence_param(cls):
        return 'Wheight'
