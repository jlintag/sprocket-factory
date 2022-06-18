# Sprocket Factory API

Installation and requirements may vary on different OSes. The setup guide is strictly for a macOS development machine.

## Required installation:
- Install at least [Python 3.9](https://www.python.org/downloads/release/python-390/)
- Install [poetry](https://python-poetry.org/docs/)
- Run `poetry install` to install dependencies found in `pyproject.toml`

## Running the app
All commands are run from the root directory

### Run app locally for development
- `poetry run uvicorn src.api.main:app --reload`

### Run app via `docker` for development
- `docker build -t sprocket-factory-api .`
- `docker run -it -p 8000:8000 --rm --name sprocket-factory-api sprocket-factory-api:latest`
  
### Run app via `docker compose` for development
- `docker compose up --build`

### Run tests
- `poetry run pytest`

## Database Shenanigans
### Flow
In order to migrate the seeded data from JSON to Postgres table, the JSON needed to be sanitized of unnecessary characters and fed into Postgres using an init sql file.
### Manually accessing a running postgres instance (whether by `docker compose` or some other mechanism)
- Either install postgres on local machine or just [`psql`](https://stackoverflow.com/questions/44654216/correct-way-to-install-psql-without-full-postgres-on-macos)
- Run `psql -h 0.0.0.0 -p 5432 -U postgres` and enter the password for your instance (also just `postgres` if running from `docker compose`)