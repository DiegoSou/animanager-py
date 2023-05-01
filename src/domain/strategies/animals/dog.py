from src.domain.strategies.interface import AnimalStrategyInterface

class DogStrategy(AnimalStrategyInterface):
    """Define a ação de produção e parâmetro de competência para cachorro"""

    @classmethod
    def action(cls):
        return 'Yap'

    @classmethod
    def competence_param(cls):
        return 'Fur'
