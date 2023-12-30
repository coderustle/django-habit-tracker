#!/usr/bin/env python

import subprocess
from dataclasses import dataclass
from random import choice
from string import ascii_letters, digits
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


@dataclass
class EnvVar:
    name: str
    value: str


def main():
    """
    This function create the .env file with the needed
    environment variables.
    """
    secret = "".join(choice(ascii_letters + digits) for _ in range(50))
    environments = [
        EnvVar(
            name="AZURE_STORAGEACCOUNT",
            value="",
        ),
        EnvVar(
            name="AZURE_ACCOUNTKEY",
            value="",
        ),
        EnvVar(
            name="AWS_ACCESS_KEY_ID",
            value="AKIAxxxxxxxxxxxxxxxx",
        ),
        EnvVar(
            name="AWS_ACCESS_KEY",
            value="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxx"
        ),
        EnvVar(
            name="DB_REPLICA_URL",
            value="abs://account@container/prod.sqlite3",
        ),
        EnvVar(
            name="BUCKETNAME",
            value="",
        ),
        EnvVar(
            name="DB_PATH",
            value="/app/database/prod.sqlite3",
        ),
        EnvVar(
            name="DB_REPLICA_PATH",
            value="/data/database/prod.sqlite3",
        ),
        EnvVar(
            name="SECRET_KEY",
            value=secret,
        ),
        EnvVar(
            name="DJANGO_SETTINGS_MODULE",
            value="habitstacker.settings.dev",
        ),
    ]

    # Create .env file
    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        for var in environments:
            env.write(f"{var.name}={var.value}\n")

    subprocess.run(["yarn", "install"], shell=True)
    subprocess.run(["yarn", "build:prod"])
    subprocess.run(["pre-commit", "install"], shell=True)
    subprocess.run(["python", "manage.py", "migrate"])


if __name__ == "__main__":
    main()
