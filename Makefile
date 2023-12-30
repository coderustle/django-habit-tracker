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
	--env DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
	--env DB_PATH=$(DB_PATH) \
	--env DB_REPLICA_PATH=$(DB_REPLICA_PATH) \
	-p 8000:8000 habitstacker:dev
