from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django_htmx.http import HttpResponseClientRedirect
from guardian.shortcuts import get_objects_for_user, assign_perm
from django.views.decorators.http import require_http_methods

from .forms import AddHabitForm


@login_required
def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page after user successfully login.
    """
    template = "habits/home.html"
    if request.htmx:
        template = "habits/partials/home.html"

    habits = get_objects_for_user(request.user, "habits.view_habit")

    return TemplateResponse(request, template, {"habits": habits})


@login_required
@require_http_methods(["GET", "POST"])
def add_habit(request: HttpRequest) -> HttpResponse:
    """
    This view handle the add habit form
    """
    template = "habits/partials/add_habit.html"

    if request.method == "GET":
        form = AddHabitForm()
        return TemplateResponse(request, template, {"form": form})

    if request.method == "POST":
        form = AddHabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            assign_perm("habits.view_habit", request.user, habit)
            return HttpResponseClientRedirect(reverse("habits:home"))
        else:
            return TemplateResponse(request, template, {"form": form})


@login_required
def edit_habit(request: HttpRequest, id: int) -> HttpResponse:
    pass


@login_required
def delete_habit(request: HttpRequest, id: int) -> HttpResponse:
    pass


@login_required
def list_habit(request: HttpRequest) -> HttpResponse:
    """
    This function handle the request to list all habit.
    """


@login_required
def log_habit(request: HttpRequest) -> HttpResponse:
    pass
