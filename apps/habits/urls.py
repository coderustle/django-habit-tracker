from django.urls import path

from .views import add_habit, home, log_habit

app_name = "habits"

urlpatterns = [
    path("home/", view=home, name="home"),
    path("add/", view=add_habit, name="add"),
    path("log/<int:pk>", view=log_habit, name="log"),
]
