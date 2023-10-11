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
