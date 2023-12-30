# Habit Stacker

[![Production](https://github.com/coderustle/habitstacker/actions/workflows/prod.yml/badge.svg)](https://github.com/coderustle/habitstacker/actions/workflows/prod.yml) [![Development](https://github.com/coderustle/habitstacker/actions/workflows/dev.yml/badge.svg)](https://github.com/coderustle/habitstacker/actions/workflows/dev.yml)

Habit Stacker is a simple, user-friendly web application to help users track and maintain their daily habits.

## Features

- **User Authentication:** Register, log in, and manage your profile. (WIP)
- **Habit Management:** Add, edit, and delete habits. (WIP)
- **Daily Tracking:** Mark habits as completed for each day. (WIP)
- **Statistics:** Visualize your progress over time. (WIP)
- **Reminders:** Set daily reminders to ensure you don’t break the chain. (WIP)

## Technology stack

- Django
- Htmx
- Tailwindcss
- Webpack
- SQLite
- Litestream

## Run it locally using Docker

1. Clone the repository `git clone https://github.com/coderustle/habitstacker.git`
2. Change directory `cd habitstacker`
3. Create a Python environment `python -m venv .venv`
4. Activate virtual environment `source .venv/bin/activate`
5. Generate `.env` file by running `./script/bootstrap.py`
6. Build development container `make dev-build`
7. Run development container `make dev-run`

## Environment variables

```bash
# OPTIONAL: Azure Storage Account Name
AZURE_STORAGEACCOUNT=
# OPTIONAL: Azure Storage Account Key 
AZURE_ACCOUNTKEY=
# OPTIONAL: AWS Access Key ID
AWS_ACCESS_KEY_ID=AKIAxxxxxxxxxxxxxxxx
# OPTIONAL: AWS Access Key Secret
AWS_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxx
# OPTIONAL: Azure Storage Container name or AWS Bucket name 
BUCKETNAME=
# REQUIRED: Path where database is stored. Default is app root folder.
DB_PATH=/app/database/prod.sqlite3
# REQUIRED: The full path of the replica database (AWS,Azure or Local)
DB_REPLICA_PATH=/data/database/prod.sqlite3
# REQUIRED: Django secret key
SECRET_KEY=O1Kn8GzxXSEA5IBxj19fKTz15rQU2RWpVcMXV2D8GU4ZSATNk7
# Required: Django app settings
DJANGO_SETTINGS_MODULE=habitstacker.settings.dev
```
