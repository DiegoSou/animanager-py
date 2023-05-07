from abc import ABC, abstractmethod

class AnimalStrategyInterface(ABC):

    @classmethod
    @abstractmethod
    def action(cls):
        """animal action product: eggs, milk, etc"""

    @classmethod
    @abstractmethod
    def competence_param(cls):
        """animal competence characteristics: vlocity, production_per_week"""
