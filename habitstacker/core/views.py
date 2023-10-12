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


@login_required
def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page after user successfully login.
    """
    template = "core/home.html"
    if request.htmx:
        template = "core/partials/home.html"

    return TemplateResponse(request, template)
