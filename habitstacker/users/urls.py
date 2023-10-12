from django.urls import path

from .views import user_register

app_name = "users"

urlpatterns = [
    path("register/", view=user_register, name="register"),
]
