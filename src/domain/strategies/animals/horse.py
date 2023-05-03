from src.domain.strategies.interface import AnimalStrategyInterface

class HorseStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para cavalo"""

    @classmethod
    def action(cls):
        return 'Gallop'

    @classmethod
    def competence_param(cls):
        return 'Velocity'
