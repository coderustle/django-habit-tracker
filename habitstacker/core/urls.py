from django.urls import path

from .views import index, home, navbar

app_name = "core"

urlpatterns = [
    path("", view=index, name="index"),
    path("home/", view=home, name="home"),
    path("navbar/", view=navbar, name="navbar"),
]
