from django.urls import path

from .views import user_login, user_logout, user_register

app_name = "users"

urlpatterns = [
    path("register/", view=user_register, name="register"),
    path("login", view=user_login, name="login"),
    path("logout/", view=user_logout, name="logout"),
]
