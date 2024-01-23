# syntax=docker/dockerfile:1

# requirements.txt file to install in virtual environment
ARG PYTHON_VERSION=python:3.12-slim-bookworm

# ********************************************************
# * BUNDLE STATIC FILES                                  *
# ********************************************************
FROM node:lts-bookworm AS bundle

ENV NODE_ENV=production

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Enable yarn
RUN corepack enable

# Install packages
RUN yarn install --frozen-lockfile && yarn run build:prod

# ********************************************************
# * BUILD PYTHON VIRTUAL ENVIRONMENT - BASE IMAGE        *
# ********************************************************
FROM ${PYTHON_VERSION} AS base

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the system
RUN --mount=type=cache,target=/var/cache/apt-base \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Create virtual environment
RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Install python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download the static build of Litestream directly into the path & make it executable.
# This is done in the builder and copied as the chmod doubles the size.
ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz

# ********************************************************
# * BUILD PRODUCTION APP                                 *
# ********************************************************
FROM ${PYTHON_VERSION} as production

RUN --mount=type=cache,target=/var/cache/apt-production \
    apt-get update

# Set the working directory
WORKDIR /app

# Copy config files
COPY ./scripts/file_litestream.yml /etc/litestream.yml

# Copy binaries from base
COPY --from=base /opt/venv /opt/venv
COPY --from=base /usr/local/bin/litestream /usr/local/bin/litestream

# Copy staticfiles from base
COPY --from=bundle /app/habitstacker/static /app/habitstacker/static
COPY --from=bundle /app/webpack-stats.json /app/webpack-stats.json

ENV PATH="/opt/venv/bin:$PATH"

# Copy the project files
COPY . .

# Expose django port
EXPOSE 8000

# Entrypoint
ENTRYPOINT [ "scripts/init.sh" ]
