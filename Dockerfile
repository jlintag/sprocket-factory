###############################################
# Base Image
###############################################
FROM python:3.9-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="/root/.local/bin:$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base as builder-base
RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# get around requiring 'cleo' module
RUN ln -s $POETRY_HOME/lib/poetry/_vendor/py3.8 $POETRY_HOME/lib/poetry/_vendor/py3.9

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

###############################################
# Dev Image
###############################################
FROM python-base as development
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY ./backend-python-api/api /src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]

# ###############################################
# # Production Image
# ###############################################
# FROM python-base as production
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
# COPY ./src /src/
# CMD ["uvicorn", "backend-python-api.main:app", "--host", "0.0.0.0", "--port", "80"]