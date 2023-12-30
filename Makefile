ifneq (,$(wildcard ./.env))
    include .env
    export
endif

#--------------------------------------------------------
# Docker commands
#--------------------------------------------------------
build:
	docker build . --target production \
	--build-arg SECRET_KEY=$(SECRET_KEY) \
	--build-arg DJANGO_SETTINGS_MODULE=habitstacker.settings.prod \
	--build-arg PYTHON_REQUIREMENTS_FILE=prod \
	--no-cache \
	--tag habitstacker:prod

run:
	docker run --name habitstacker -it --rm \
	--env SECRET_KEY=$(SECRET_KEY) \
	--env DJANGO_SETTINGS_MODULE=habitstacker.settings.prod \
	--env DB_PATH=$(DB_PATH) \
	--env DB_REPLICA_PATH=$(DB_REPLICA_PATH) \
	--entrypoint /bin/bash \
	-p 8000:8000 habitstacker:prod

#--------------------------------------------------------
# Litestream commands
#--------------------------------------------------------
restore:
	litestream restore -v -if-database-exists -o ./database/db.sqlite3 \
	$(REPLICA_URL)
