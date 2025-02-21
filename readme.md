## Python linting pipeline 
This demo project demo is used for a Medium article.


### Project Structure
The project follows the modular and functional principles. 

- **docs**: Contains documentation for the project on the app.
- **src**: Contains base project  
    - **/core**: Contains the base business logic of features in the app - sorted by entities/features e.g. events, log, sentry, azure, aws, etc.
    - **/demo**: Contains demo tasks or scripts implementing modules from `core/`.
 - **tests**: Contains tests for the application (e.g. integration test, unit test, end to end test)
 - **logs**: Directory used for logfile storage
 - **shell**: Utility scripts for cleaning cache and logs

### Usage
To use this project, follow these steps:

1. Clone the repository.

2. Run the setup script `/shell/setup.sh ` and insert correct .env vars.

3. Install the Python packages by running command;

- For Development `pip install --editable . `
- For Production `pip install . `

4. Run your wanted python scripts from `/src/demo` dir. 

### Testing
This project uses pytest for testing. All tests are present and located in the `tests/` dir. 

Run all tests by the following command: `python -m pytest`.

Run single test by the following command: `python -m tests/test_mytest.py`. 

### How to run shell scripts
In the `/shell` directory two shell-scripts are present for cleaning the project.

Run the scripts by the following command: `./name_of_script.sh`.

### Static Code Analytics, formatting and linting
To keep a clean and unified codebase we strive to use [Ruff](https://docs.astral.sh/ruff/).

Format code: `python -m ruff format .`

Scan code: `python -m ruff check .`

Scan and fix code: `python -m ruff check . --fix`

For SQL sanity checks we strive to use [sqlfluff](https://github.com/sqlfluff/sqlfluff)

Scan database queries: `python -m sqlfluff lint . --dialect ansi`

Format database queries: `python -m sqlfluff fix . --dialect ansi`
