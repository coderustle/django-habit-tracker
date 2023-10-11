from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    A custom user model that extends Django's built-in AbstractUser model.
    """

    class Meta:
        db_table = "auth_user"

    def __str__(self) -> str:
        return self.username
