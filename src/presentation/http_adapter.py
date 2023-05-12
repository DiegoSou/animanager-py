from typing import Type
from src.presentation.interface import RouteInterface
from .http_models import HttpRequest, HttpResponse

def flask_adapter(request: any, controller: Type[RouteInterface]) -> any:
    """
    Adapt flask requests
    - params
        - request: the flask route request
        - route: a controller implementation with route() method
    - return
        - HttpResponse with results or error
    """

    header = request.headers
    query = request.args
    form = request.form
    files = request.files
    body = None

    if (request.method == 'POST') and (header.get('Content-Type') == 'application/json'):
        body = request.get_json()

    http_request = HttpRequest(header, body, query, form, files)

    # route should catch any exceptions
    return controller.route(http_request)
    