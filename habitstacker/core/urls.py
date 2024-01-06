from django.urls import path

from .views import index, navbar

app_name = "core"

urlpatterns = [
    path("", view=index, name="index"),
]
