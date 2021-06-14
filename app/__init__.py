from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


# Initializing application
def create_app(config_name):
    app = Flask(__name__)

 # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)