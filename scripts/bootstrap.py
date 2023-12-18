#!/usr/bin/env python

import logging
import random
import string
import subprocess
from dataclasses import dataclass
from random import choice
from string import ascii_letters, digits
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()


PROJECT_ROOT = Path(__file__).parent.parent


@dataclass
class EnvVar:
    name: str
    value: str


def create_environment_variables():
    """
    This function create the .env file with the needed
    environment variables.
    """
    secret = "".join(choice(ascii_letters + digits) for _ in range(50))
    environments = [
        EnvVar(name="LITESTREAM_AZURE_ACCOUNT_KEY", value=""),
        EnvVar(name="DB_REPLICA_URL", value=""),
        EnvVar(name="DB_STORAGE_ACCOUNT", value=""),
        EnvVar(name="DB_CONTAINER", value=""),
        EnvVar(name="DB_PATH", value=""),
        EnvVar(name="DB_NAME", value=""),
        EnvVar(name="SECRET_KEY", value=secret),
        EnvVar(
            name="DJANGO_SETTINGS_MODULE", value="habitstacker.settings.dev"
        ),
    ]

    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        for var in environments:
            env.write(f"{var.name}={var.value}\n")


def init_node_environment():
    """
    Run yarn install
    """
    subprocess.run(["yarn", "install"], shell=True)


def generate_staticfiles():
    """
    Run yarn build:prod
    """
    subprocess.run(["yarn", "build:prod"])


def install_pre_commit():
    """
    Run pre-commit install
    """
    subprocess.run(["pre-commit", "install"], shell=True)


def run_db_migrations():
    """
    Run `python manage.py migrate`
    """
    subprocess.run(["python", "manage.py", "migrate"])


def main():
    logger.info("Create .env file")
    create_environment_variables()
    logger.info("Install node packages")
    init_node_environment()
    logger.info("Generate static files")
    generate_staticfiles()
    logger.info("Run db migrations")
    run_db_migrations()
    logger.info("Install pre-commit")
    install_pre_commit()


if __name__ == "__main__":
    main()
