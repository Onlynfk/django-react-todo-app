# django-react-todo-app

A fully functional todo django/react app >> Work in Progress 😊


## Getting Started
1. Install [Python](https://www.python.org/downloads/), [Yarn](https://classic.yarnpkg.com/en/docs/install/),
2. Clone the repo
```
$ git clone https://github.com/Onlynfk/django-react-todo-app.git
$ cd django-react-todo-app
```
3. Install [pipenv](https://pypi.org/project/pipenv/), a python virtual environment manager. Install backend dependencies and run migrations to create database. Default database is SQLite.

* Before you are should open two terminals one for backend and another for forntend

4. Now ensure you are in root directory to install the backend servers (first terminal)
```  
$ pipenv shell
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
4. Now Install frontend dependencies and run watch frontend (second terminal)
```
$ cd frontend
$ yarn install or npm install
$ npm run dev
```
5. View on your browser ( to see the it's working)
```
http://127.0.0.1:8000/frontend/

```

