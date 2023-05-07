from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers import HttpRequest, HttpResponse

class RouteInterface(ABC):

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """Define a route"""
