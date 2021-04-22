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
``
` ensure you are in root directory 
$ pipenv shell
$ pip install -r requirements.txt
$ python manage.py migrate
```
4. Install frontend dependencies.
```
$ cd frontend
$ yarn install or npm install
```
5. Run the frontend  with following commands in appropriate directories.
```
$ npm install
$ npm run dev
```
5. Run the backend servers with following commands in appropriate directories.
```
$ python manage.py runserver

```
