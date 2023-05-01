from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import animals


class IRegisterAnimal(ABC):
    
    @abstractmethod
    def register(self, animal:str, name: str, specification: Dict[str, str]) -> Dict[bool, tuple]:
