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
            response = self.find_animal_use_case.find()
        else:
            query_keys = http_request.query.keys()

            animal_id = http_request.query['id'] if 'id' in query_keys else None
            animal_name = http_request.query['name'] if 'name' in query_keys else None
            animal_type = http_request.query['animal_type'] if 'animal_type' in query_keys else None

            response = self.find_animal_use_case.find(
                animal_id=animal_id,
                animal_name=animal_name,
                animal_type=animal_type
            )

        if response["success"]:
            return HttpResponse(status_code=200, body=response["data"])

        print(response["data"])
        return HttpResponse(status_code=500, body=response["data"])
