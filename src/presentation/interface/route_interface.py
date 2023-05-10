from typing import Type
from abc import ABC, abstractmethod
from src.presentation import HttpRequest, HttpResponse

class RouteInterface(ABC):

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """
        Define a route
        - params
            - http_request: an adapted HttpRequest class
        - return
            - Adapted HttpResponse with results from a specific implementation of route
        """
