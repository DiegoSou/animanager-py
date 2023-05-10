from typing import Type
from src.presentation.interface import RouteInterface
from .http_models import HttpRequest, HttpResponse

def flask_adapter(request: any, route: Type[RouteInterface]) -> any:
    """
    Adapt flask requests
    - params
        - request: the flask route request
        - route: a controller implementation with route() method
    - return
        - HttpResponse with results or error
    """

    try:
        header = request.headers
        body = None
        query = request.args
        form = request.form

        if (request.method == 'POST') and (header.get('Content-Type') == 'application/json'):
            body = request.get_json()

        http_request = HttpRequest(
            header=header,
            body=body,
            query=query,
            form=form
        )

        # chama route da controller que foi passada
        response = route.route(http_request)
        return response

    except Exception as exc:
        print(exc)
        return HttpResponse(status_code=500, body="Unexpected error")
    