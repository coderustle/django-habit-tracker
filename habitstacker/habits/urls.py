from django.urls import path

from .views import home

app_name = "habits"

urlpatterns = [
    path("home/", view=home, name="home"),
]
