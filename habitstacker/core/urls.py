from django.urls import path

from .views import index

app_name = "core"

urlpatterns = [
    path("", view=index, name="index"),
    path("home/", view=index, name="home"),
]
