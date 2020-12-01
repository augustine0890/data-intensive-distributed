#### Project Overview
**API Features**
- List all known planets
- Register new users
- Anthenticate existing users
- Add new planetary discoveries to the database
- Update existing planetary data
- Delete planets when necessary

**Create enviroment**
- `python3 -m venv env`

**Active**
- `source env/bin/activate`

**Deactivae**
- `deactivate`

**Update pip**
- `pip install --upgrade pip`
- `pip list`

**Install Flask**
- `pip install flask`

#### App structure
- `pip freeze > requirements.txt`
- For installing packages: `pip install -r requirements.txt`

**Creating a Flask app**
- `touch app.py`

- `__name__` is a special variable used by the Python interpreter to understand if a file is the main program.

**Running the Flask app**
- `python3 app.py`
- Stop the app by hitting `Ctrl + c`

**Flask environment variables**
- Running `export FLASK_APP=app.py` will set the `FLASK_APP` variable to `app.py`
- Running `export FLASK_ENV=development` tells Flask we want to run our app in development mode
- Warning: never run a live Flask application in production using development mode
- `flask run`
- To deactivate your virtual environment: `deactivate`
