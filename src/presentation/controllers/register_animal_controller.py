from typing import Type
from src.presentation.interface import RouteInterface
from src.presentation import HttpRequest, HttpResponse
from src.domain.usecases import IRegisterAnimalUseCase

class RegisterAnimalController(RouteInterface):

    def __init__(self, use_case: Type[IRegisterAnimalUseCase]):
        self.register_animal_use_case = use_case

    def route(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """Route to register an animal"""
        response = None

        if http_request.form:
            response = self.register_animal_use_case.register_animal(
                name=http_request.form["name"],
                sex=http_request.form["sex"],
                weight=http_request.form["weight"],
                specie=http_request.form["specie"],
                animal_type=http_request.form["animal_type"]
            )

        if http_request.files:
            response = self.register_animal_use_case.upload_animals(
                file_data=http_request.files["file"]
            )

        if response["success"]:
            return HttpResponse(status_code=201, body=response["data"])

        return HttpResponse(status_code=500, body=response["error"])
