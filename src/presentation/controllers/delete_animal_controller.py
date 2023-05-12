from typing import Type
from src.presentation.interface import RouteInterface
from src.presentation import HttpRequest, HttpResponse
from src.domain.usecases import IDeleteAnimalUseCase

class DeleteAnimalController(RouteInterface):

    def __init__(self, use_case: Type[IDeleteAnimalUseCase]):
        self.delete_animal_use_case = use_case

    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """Route to delete an animal"""

        response = None

        if http_request.query:
            response = self.delete_animal_use_case.delete_animal(
                animal_id=http_request.query["id"]
            )

        if response["success"]:
            return HttpResponse(status_code=200, body=response["data"])

        print(response["data"])
        return HttpResponse(status_code=500, body=response["data"])
