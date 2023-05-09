from typing import Type
from src.presentation.interface import RouteInterface
from src.presentation import HttpRequest, HttpResponse
from src.domain.usecases import IFindAnimalUseCase

class FindAnimalController(RouteInterface):

    def __init__(self, use_case: Type[IFindAnimalUseCase]) -> None:
        self.find_animal_use_case = use_case

    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """Route to find animals"""
        response = None

        if not http_request.query:
            response = self.find_animal_use_case.find_all()

        return HttpResponse(status_code=200, body=response["data"])
