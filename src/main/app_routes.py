from flask import jsonify, request, Blueprint
from src.main.composers import find_animal_composite
from src.main.adapter import flask_adapter

animals_routes = Blueprint("animals", __name__)

@animals_routes.route("/animals", methods=["GET", "POST"])
def index():
    "get data from animals"

    response = flask_adapter(request, find_animal_composite())

    if response.status_code < 300:
        return jsonify({"data": response.body}), response.status_code

    return jsonify({
        "error": {
            "stauts": response.status_code,
            "title": response.body
        }
    }), response.status_code
