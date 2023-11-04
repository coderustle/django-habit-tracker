from django.contrib.auth.decorators import login_required
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


@login_required
def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page after user successfully login.
    """
    template = "core/home.html"
    if request.htmx:
        template = "core/partials/home.html"

    return TemplateResponse(request, template)
