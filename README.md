# Basic Flask Application
This is a basic and containerized Flask application to help start coding using Flask in the backend.

## Application Setup
> **Required:** `docker` and `docker-compose` must be installed in your machine. 

### Technologies
- Docker e Docker compose
- Python + Flask + Flask-SQLAlchemy (ORM)
- Postgresql

### Images
- [postgres:10-alpine](https://hub.docker.com/_/postgres)
- [python:3.11-slim-buster](https://hub.docker.com/_/python)
- [adminer](https://hub.docker.com/_/adminer)

### Containers
- `web`: backend module running the flask application.
- `db`: database containers running the postgresql db
- `adminer`: database admin similiar to phpMyAdmin

### How to run the Flask application
> Run the following commands in the root directory.
**Commands:**
- Create .env file base on `.env.dist`: `cp .env.dist .env`
- Start containers: `docker-compose up` (use `-d` aferter up to start the container in the background)
- Stop containers: `docker-compose down`

**Migrations**
> - Run the following lines when needs to manage migrations:
> - Usage: `flask db [OPTIONS] COMMAND [ARGS]...`
- `flask db init`: to create a folder with set to migration.
- `flask db migrate -m "Initial migration."`: to generate a migration.
- `flask db [upgrade|downgrade]`: to up/down changes based on migration files.
- `flask db --help`: Show database help message.

**Tips**
-  `__init__.py` files means that the directory is a package
- In `.env`:
    - `SECRET_KEY`: This is a secret key to secure your session data and cookies of your application
    - `FLASK_DEBUG`: It must be `False` when you deploy your application to `Production`


### **URLs**
- Flask App: http://localhost:8000/
- Adminer: http://localhost:8080/

### Resources
- [Flask doc](https://flask.palletsprojects.com/en/2.2.x/)
- [About Flask app environment configuration](https://flask.palletsprojects.com/en/2.2.x/config/)
- [Flask SQLAlchemy doc](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)