ifneq (,$(wildcard ./.env))
    include .env
    export
endif

#--------------------------------------------------------
# Docker commands
#--------------------------------------------------------
build-dev:
	docker build . --target development \
	--build-arg SECRET_KEY=$(SECRET_KEY) \
	--build-arg DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
	--build-arg PYTHON_REQUIREMENTS_FILE=dev \
	--no-cache \
	--tag habitstacker:dev

run-dev:
	docker run --name habitstacker -it --rm \
	-p 8000:8000 habitstacker:dev bash