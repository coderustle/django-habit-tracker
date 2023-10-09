from django.urls import path

from .views import hello_world

app_name = "core"

urlpatterns = [
    path("", view=hello_world, name="index"),
]
