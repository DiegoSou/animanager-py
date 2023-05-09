from flask import jsonify, request, Blueprint, redirect, render_template
from src.main.composers import find_animal_composite, register_animal_composite
from src.presentation import flask_adapter

animals_routes = Blueprint("animals", __name__)

@animals_routes.route("/animals", methods=["GET", "POST"])
def index():
    "animals index template"

    if request.method == "GET":
        response = flask_adapter(request, find_animal_composite())
    if request.method == "POST":
        response = flask_adapter(request, register_animal_composite())


    if response.status_code < 300:
        return render_template("animals_index.html")


    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code
