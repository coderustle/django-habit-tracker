ifneq (,$(wildcard ./.env))
    include .env
    export
endif

#--------------------------------------------------------
# Docker commands
#--------------------------------------------------------
dev-build:
	docker build . --target development \
	--build-arg SECRET_KEY=$(SECRET_KEY) \
	--build-arg DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
	--build-arg PYTHON_REQUIREMENTS_FILE=dev \
	--no-cache \
	--tag habitstacker:dev

dev-run:
	docker run --name habitstacker -it --rm \
	-p 8000:8000 habitstacker:dev bash


prod-build:
	docker build . --target production \
	--build-arg SECRET_KEY=$(SECRET_KEY) \
	--build-arg DJANGO_SETTINGS_MODULE=habitstacker.settings.prod \
	--build-arg PYTHON_REQUIREMENTS_FILE=prod \
	--no-cache \
	--tag habitstacker:prod

prod-run:
	docker run --name habitstacker -it --rm \
	--env-file ./.env \
	-p 8000:8000 habitstacker:prod bash


#--------------------------------------------------------
# Litestream commands
#--------------------------------------------------------
restore:
	litestream restore -v -if-database-exists -o ./database/db.sqlite3 \
	$(REPLICA_URL)
