#### Create enviroment
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
- `mkdir app`
- `pip freeze > requirements.txt`
- For installing packages: `pip install -r requirements.txt`

**Virtual Enviroment with `virtualenv`**
- `pip install virtualenv`

#### Deploy the Website
- Download and install Heroku Toolbelt from www.toolbelt.heroku.com/
    - `brew tap heroku/brew && brew install heroku`
- Login with Heroku
    - `heroky login`
- Create the app in Heroku
    - `heroku create <app-name>` #augustine-blog
    - `https://augustine-blog.herokuapp.com/`
    - `https://git.heroku.com/augustine-blog.git`
    - Check your apps: `heroku apps`
- Install gunicorn
    - `pip install gunicorn`
- Create a file named `"Procfile"` in the main app directory
- Then type in this line inside:
    `"web: gunicorn app:app"` where `"app"` should be replaced with the name of your Python script and `"app"` with the name of the variable holding your Flask app.
- Create a `runtime.txt` file in the main app directory and type `"python-3.7.6" inside.
- Initialize a local git repository
    - `git init`
- Add your local application files to git
    - `git add .`
- Commit the changes
    - `git commit -m "<commit-message>"`
- Tell heroku the name of the app you want to use
    - `heroku git:remote --app <app-name>` #augustine-blog
- Push the changes to Heroku
    - `git push heroku master`
- Go ahead and open your app with `heroku open`.
- `heroku info`
- Access the server logs: `heroku logs`