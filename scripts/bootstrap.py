#!/usr/bin/env python

import logging
import random
import string
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()


PROJECT_ROOT = Path(__file__).parent.parent


def create_environment_variables():
    """
    This function create the .env file with the needed
    environment variables.
    """
    secret = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(50)
    )
    environments = f"""
    PYTHON_REQUIREMENTS_FILE=dev
    DJANGO_SETTINGS_MODULE=habitstacker.settings.dev
    SECRET_KEY={secret}
    DJANGO_DEBUG=True
    REPLICA_URL=abs://coderustle@database/habitstacker/db.sqlite3
    LITESTREAM_AZURE_ACCOUNT_KEY=op://Development/coderustle-storage-account-key/credential
    DATABASE_PATH=./database/db.sqlite3
    """
    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        env.write(environments)


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
