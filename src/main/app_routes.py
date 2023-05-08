from flask import jsonify, request, Blueprint, render_template, url_for, redirect
from src.main.composers import find_animal_composite, register_animal_composite
from src.main.adapter import flask_adapter

animals_routes = Blueprint("animals", __name__)

@animals_routes.route("/animals", methods=["GET"])
def index():
    "get animals data"
    response = flask_adapter(request, find_animal_composite())

    if response.status_code < 300:
        return jsonify({"data": response.body}), response.status_code

    return jsonify({
        "error": {
            "stauts": response.status_code,
            "title": response.body
        }
    }), response.status_code


@animals_routes.route("/animals/form", methods=["GET", "POST"])
def register():
    "insert animals data"

    if request.method == "GET":
        return render_template("index.html")

    response = flask_adapter(request, register_animal_composite())

    if response.status_code < 300:
        return redirect("http://localhost:5000/animals")

    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code
