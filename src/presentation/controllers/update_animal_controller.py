from typing import Type
from src.presentation.interface import RouteInterface
from src.presentation import HttpRequest, HttpResponse
from src.domain.usecases import IUpdateAnimalUseCase

class UpdateAnimalController(RouteInterface):

    def __init__(self, use_case: Type[IUpdateAnimalUseCase]):
        self.update_animal_use_case = use_case

    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """Route to update an animal"""

        response = None

        if http_request.form:
            response = self.update_animal_use_case.update_animal(
                animal_id=http_request.form['id'],
                name=http_request.form['name'],
                weight=http_request.form['weight'],
                specie=http_request.form['specie']
            )

        if response["success"]:
            return HttpResponse(status_code=204, body=response["data"])

        return HttpResponse(status_code=500, body=response["error"])
