from abc import ABC, abstractmethod
from typing import Any

class DataExtractor(ABC):

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.extractdata()(*args, **kwds)

    @abstractmethod
    def extractdata(self, func = None) -> callable:
        """recebe função que define como extrair os dados como parametro"""
        def intermediaria(*args, **kwargs):
            return func(*args, **kwargs)
        return intermediaria
