# CoffeeApp

This is a Python project for tracking who is offering pride related coffee specials.  
## Prerequisites
Before setting up the project, make sure you have the following installed:
- [pyenv](https://github.com/pyenv/pyenv)
- [poetry](https://python-poetry.org/)
## Setup
1. Clone the repository:

	```bash
	git clone https://github.com/your-username/CoffeeApp.git
	```
2. Navigate to the project directory:

	```bash
	cd CoffeeApp
	```
3. Set up the Python environment using pyenv:

	```bash
	pyenv install 3.9.18
	pyenv local 3.9.18
	```
4. Install project dependencies using poetry:

	```bash
	poetry install
	```
5. Start the application:

	```bash
	poetry run uvicorn main:app --reload
	```
6. Run database migrations with Alembic:

	```bash
	poetry run alembic upgrade head
	```
7. Troubleshooting:

	If you encounter an error stating that `libpq` is not found, you can follow these steps to resolve it:

	1. Install `libpq` using Homebrew:
		```bash
		brew install libpq
		```
	2. After installing `libpq`, try running the application again. If the error persists, make sure that the `libpq` library is in the correct path. You can check the library path by running:

		```bash
		pg_config | grep libpq
		```

		If the library is not listed, you may need to unlink and relink postgres and libq 

		```bash
		brew unlink postgresql@14
		brew link libpq --force
		```

	3. Rerun the migrations to see if the error is resolved

Once the application is running, you can access it at `http://localhost:8000`.
## API Docs
API docs can be accessed at `http://localhost:8000/docs`. 



Once the application is running, you can access it at `http://localhost:8000`.

## API Docs

API docs can be accessed at `http://localhost:8000/docs`. 
