from flask import jsonify, request, Blueprint, redirect, render_template, flash, url_for
from src.main.composers import (
    find_animal_composite,
    register_animal_composite,
    update_animal_composite,
    delete_animal_composite
)
from src.presentation import flask_adapter

animals_routes = Blueprint("animals", __name__)

@animals_routes.route("/animals", methods=["GET"])
def index():
    "animals index template"

    response = flask_adapter(request, find_animal_composite())

    if response.status_code < 300:
        return render_template('animals_index.html', animals_data = response.body)

    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code


@animals_routes.route("/animals", methods=["POST"])
def register():
    "animals register template"

    response = flask_adapter(request, register_animal_composite())

    if response.status_code < 300:
        flash("Animal registered on database")
        return redirect(url_for("animals.index"))

    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code


@animals_routes.route("/animals/update", methods=["POST"])
def update():
    "animals update template"

    response = flask_adapter(request, update_animal_composite())

    if response.status_code < 300:
        flash("Record updated")
        return redirect(url_for("animals.index"))

    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code


@animals_routes.route("/animals/delete", methods=["GET", "POST"])
def delete():
    "animals delete template"
    print(request.method)

    response = flask_adapter(request, delete_animal_composite())

    if response.status_code < 300:
        flash("Record deleted")
        return redirect(url_for("animals.index"))

    return jsonify({
        "error": {
            "status": response.status_code,
            "title": response.body
        }
    }), response.status_code
