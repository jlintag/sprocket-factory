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
- You'll want to source the .env file

### Run app via `docker` for development
- `docker build -t sprocket-factory-api .`
- `docker run -it -p 8000:8000 --rm --name sprocket-factory-api sprocket-factory-api:latest`
- You'll want to source the .env file or pass in an environment variable for DATABASE_URL
  
### Run app via `docker compose` for development
- `docker compose up --build`
- `docker compose down -v --rmi all --remove-orphans` to bring it down and remove volumes, containers and leftover images

### Run tests
I haven't figured out how to run unittests without a backing database quite yet, so you'll need to `docker compose up` and have the database running in order to run tests. After that, run `poetry run pytest`

## Database Shenanigans
### Flow
In order to migrate the seeded data from JSON to Postgres table, the JSON needed to be sanitized of unnecessary characters and fed into Postgres using an init sql file.
### Manually accessing a running postgres instance (whether by `docker compose` or some other mechanism)
- Either install postgres on local machine or just [`psql`](https://stackoverflow.com/questions/44654216/correct-way-to-install-psql-without-full-postgres-on-macos)
- Run `psql -h 0.0.0.0 -p 5432 -U postgres` and enter the password for your instance (also just `postgres` if running from `docker compose`)