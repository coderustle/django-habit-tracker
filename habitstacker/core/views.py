from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page"""
    template = "core/index.html"
    if request.htmx:
        template = "core/partials/index.html"

    return TemplateResponse(request, template)
