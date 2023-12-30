#!/usr/bin/env bash
#
# Set Environments
set -e

# =========================================
# Litestream restore database
# =========================================
# Restore the database if it does not already exist.
if [ -f "$DB_PATH" ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	litestream restore -v -if-replica-exists
fi

# =========================================
# Start gunicorn process
# =========================================
exec litestream replicate -exec "gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 --chdir /app habitstacker.wsgi --access-logfile '-' --error-logfile '-'"
