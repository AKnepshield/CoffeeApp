# CoffeeApp

This is a Python project for a coffee ordering application.

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
## Usage

Once the application is running, you can access it at `http://localhost:8000`.

## API Docs

API docs can be accessed at `http://localhost:8000/docs`. 
