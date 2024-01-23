"""
This module contains the configuration for the apps.users app.

The UsersConfig class is responsible for configuring the app and setting the
default auto field.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
