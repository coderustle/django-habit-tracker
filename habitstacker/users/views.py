from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods

from .forms import RegisterUserForm


@require_http_methods(["GET", "POST"])
def user_register(request: HttpRequest) -> HttpResponse:
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
        form = RegisterUserForm(request.POST)
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
            return redirect("users:login")

    return TemplateResponse(request, template, {"form": form})


@require_http_methods(["GET", "POST"])
def user_login(request: HttpRequest) -> HttpResponse:
    """
    View function that handles user registration.

    If the request method is GET, it renders the registration form.
    If the request method is POST, it validates the form data and creates a new
    user if valid.
    """
    template = "registration/login.html"
    if request.htmx:
        template = "registration/partials/login.html"

    if request.method == "GET":
        form = AuthenticationForm()
        return TemplateResponse(request, template, {"form": form})

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect("core:home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("users:login")
    messages.error(request, str(form.errors))
    return TemplateResponse(request, template, {"form": form})


def user_logout(request: HttpRequest) -> HttpResponse:
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request=request)
    return redirect("users:login")


@login_required
def user_profile(request: HttpRequest) -> HttpResponse:
    """
    View function that displays the user's profile page.
    """
    template = "users/profile.html"
    if request.htmx:
        template = "users/partials/profile.html"

    return TemplateResponse(request, template)
