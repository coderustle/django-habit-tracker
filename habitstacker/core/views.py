from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def hello_world(request: HttpRequest) -> HttpResponse:
    """Test view"""
    template = "core/index.html"
    return TemplateResponse(request, template)
