from typing import Type
from src.main.interface import RouteInterface
from src.presentation.helpers import HttpRequest, HttpResponse

def flask_adapter(request: any, route: Type[RouteInterface]) -> any:
    """Adapt flask requests"""

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

        response = route.route(http_request)
        return response

    except Exception as exc:
        print(exc)
        return HttpResponse(status_code=500, body="Unexpected error")
    