FROM python:3.9-slim as python-poetry-base

ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"


###############################################################################
# POETRY BUILDER IMAGE - Installs Poetry and dependencies
###############################################################################
FROM python-poetry-base AS python-poetry-builder
RUN apt-get update \
    && apt-get install --no-install-recommends --assume-yes curl
# Install Poetry via the official installer: https://python-poetry.org/docs/master/#installing-with-the-official-installer
# This script respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -


###############################################################################
# POETRY RUNTIME IMAGE - Copies the poetry installation into a smaller image
###############################################################################
FROM python-poetry-base AS python-poetry
COPY --from=python-poetry-builder $POETRY_HOME $POETRY_HOME
RUN groupadd --gid 1000 nonroot \
    && useradd --uid 1000 --gid 1000 --no-create-home --shell /bin/bash nonroot

FROM python-poetry

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/* \

RUN poetry --version
# Your build steps here.

# Set the working directory in the container to /app
WORKDIR /code

# Add current directory code to /app in container
ADD . /code

# Install project dependencies
RUN poetry install --no-interaction

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run the command to start uWSGI
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
