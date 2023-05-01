from src.domain.strategies.interface import AnimalStrategyInterface

class HenStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para galiha"""

    @classmethod
    def action(cls):
        return 'Egg'

    @classmethod
    def competence_param(cls):
        return 'Eggs per week'
