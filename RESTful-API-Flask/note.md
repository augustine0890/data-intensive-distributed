### Project Overview
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
- `pip install Flask-SQLAlchemy`
- `pip install flask-marshmallow`

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

#### FLASK
**Status Codes**
- All web apps are based on request-response mechanism
- Requests and responses have headers
- Headers contain useful but invisible metadata that is not obvious to your end users
- The status code in the header will tell you whether your request was successful or not

**URL Parameters**
- `http://www.fakewebsite.com/`
- `http://localhost:5000?name=Augustine&age=32`
- `http://localhost:5000/Augustine/32`

**ORM: SQLAlchemny**
- SQLite
- It's file-based database system (no server required)
- No software installation if required to use SQLite
- Use an object-relational mapper (ORM) called SQLAlchemy
- Works with Python objects, not SQL
- Allows you to switch your database easily
- Can control the structure of your database from your code, which can be managed by a revision control system like Git or Gitlab
- Supports multiple database platforms

**ORM Model Classes**
- DB Browser for SQLite
    - `brew cask install db-browser-for-sqlite`