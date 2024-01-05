from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page"""
    template = "core/index.html"
    if request.htmx:
        template = "core/partials/index.html"

    return TemplateResponse(request, template)


def navbar(request: HttpRequest) -> HttpResponse:
    """Render the navigation menu"""
    template = "_navigation.html"
    if request.htmx:
        return TemplateResponse(request, template)
    return HttpResponse()
