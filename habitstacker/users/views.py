from django.contrib import messages
from django.contrib.auth import login
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods

from .forms import RegisterUserForm


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    """
    View function that handles user registration.

    If the request method is GET, it renders the registration form.
    If the request method is POST, it validates the form data and creates a new
    user if valid.
    """
    template = "registration/register.html"
    if request.htmx:
        template = "registration/partials/register.html"

    if request.method == "GET":
        form = RegisterUserForm()
        return TemplateResponse(request, template, {"form": form})

    if request.method == "POST":
        form = RegisterUserForm()
        if form.is_valid():
            user = form.save()
            # because we have two authentication backends, Django dosen't knwo
            # which one to use when to authenticate the user
            backend = "django.contrib.auth.backends.ModelBackend"
            login(request=request, user=user, backend=backend)
            messages.success(request, "Registration successful")
            return redirect("core:home")
        else:
            messages.error(request, str(form.errors))
            print(form.errors)
            return TemplateResponse(request, template, {"form": form})

    return HttpResponse(status_code=400)
