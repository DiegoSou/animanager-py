from src.infra.entities import Animals
from flask import request, Blueprint

animals_routes = Blueprint("animals", __name__, url_prefix="/animals")

@animals_routes.route("/", methods=["GET"])
def read():
    "get data from animals"
    data = Animals.query
