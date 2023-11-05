#!/usr/bin/env bash
#
# Set Environments
set -e

# =========================================
# Litestream restore database
# =========================================
# Restore the database if it does not already exist.
if [ -f ./database/prod.sqlite3 ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	litestream restore -v -if-replica-exists -o /app/database/prod.sqlite3 "abs://stcoderustle@databases/prod.sqlite3"
fi

# =========================================
# Start gunicorn process
# =========================================
exec litestream replicate -exec "gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 --chdir /app habitstacker.wsgi --access-logfile '-' --error-logfile '-'"
