FROM cr.yandex/crpf7d5p7pfudekvcc4v/python:3.11-alpine-base AS python-base

FROM python-base AS builder-base
# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install poetry

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --without dev,test

FROM python-base AS production

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY ./src/ /app
COPY ./src/aerich.ini /app/pyproject.toml

WORKDIR /app

CMD [ "./entrypoint.sh" ]
