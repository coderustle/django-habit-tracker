from django.urls import path

from .views import home, add_habit

app_name = "habits"

urlpatterns = [
    path("home/", view=home, name="home"),
    path("add/", view=add_habit, name="add"),
]
